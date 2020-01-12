from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


class Payment(models.Model):
    country = CountryField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = PhoneNumberField()
    amount = models.DecimalField(decimal_places=2, max_digits=200000)
    description = models.CharField(max_length=100, default='product/service purchased')
    type = models.CharField(default='MERCHANT', max_length=9)
    reference = models.CharField(max_length=6)