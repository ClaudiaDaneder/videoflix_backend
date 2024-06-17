from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'street', 'zip_code', 'city', 'country']
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
        user = Customer.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user