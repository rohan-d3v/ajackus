# Standard Library imports

# Third Party imports
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator
from django import forms


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, validators=[RegexValidator(
        regex='^[0-9]{10}$')], default='123456789')
    name = models.CharField(max_length=50, default='FirstName LastName')
    pincode = models.CharField(max_length=6, 
        validators=[RegexValidator(regex='^[0-9]{6}$')], default='123456')
    # Optional Fields
    address = models.CharField(max_length=50, blank=True, default='')
    city = models.CharField(max_length=50, blank=True, default='')
    state = models.CharField(max_length=50, blank=True, default='')
    country = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, **kwargs):
        super().save()
