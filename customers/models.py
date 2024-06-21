from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    street = models.CharField(max_length=150, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=100,blank=True, null=True)
    notes = models.TextField(max_length=1500, blank=True, null=True)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.username
