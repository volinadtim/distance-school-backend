from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    avatar = models.ImageField()
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    REQUIRED_FIELDS = ['first_name', 'password']
