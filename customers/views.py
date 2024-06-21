
from customers.tasks import send_activation_email
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist



class LoginView(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        customer = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=customer)
        return Response({
            'token': token.key,
            'customer_id': customer.pk,
            'email': customer.email
        })

class RegisterView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()

            customers_group, created = Group.objects.get_or_create(name='Customers')
            customer.groups.add(customers_group)

            customer.is_active = False
            customer.save()

            customer.generate_activation_token()
            send_activation_email(customer)

            return Response({
                'id': customer.id,
                'username': customer.username,
                'email': customer.email,
                'activation_token': customer.activation_token
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ActivateAccountView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data.get('activation_token')

        if not token:
            return Response({'error': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Customer.objects.get(activation_token=token)  # Beispiel: auth_token als Feld für den Token im User-Modell
        except ObjectDoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_404_NOT_FOUND)

    # Aktiviere das Benutzerkonto, indem z.B. ein Feld in der Datenbank gesetzt wird
        user.is_active = True
        user.save()

        return Response({'success': 'Account activated successfully'}, status=status.HTTP_200_OK)
