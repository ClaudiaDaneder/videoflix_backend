from django.shortcuts import render
from rest_framework import viewsets
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

            customers_group = Group.objects.get(name='Customers')
            customer.groups.add(customers_group)

            token = Token.objects.create(user=customer)
            return Response({
                'customer_id': customer.id,
                'username': customer.username,
                'email': customer.email,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)