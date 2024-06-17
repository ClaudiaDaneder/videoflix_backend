from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'street', 'zip_code', 'city', 'country')
        extra_kwargs = {
            'username': {
                'required': True
                },
            'first_name': {
                'required': True
                },
            'last_name': {
                'required': True
                },
            'email': {
                'required': True
                },
            'password': {
                'write_only': True
                }
            }


    def create(self, validated_data):
        user = Customer.objects.create_user(**validated_data)
        return user