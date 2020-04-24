from django.contrib.auth.models import AbstractUser
from django.db import models


# Basic Model
class CustomUser(AbstractUser):
    TYPES_PROF = (
        ('D', 'Director'),
        ('S', 'Student'),
        ('T', 'Teacher'),
        ('P', 'Parent'),
    )

    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(blank=True, max_length=255)
    surname = models.CharField(max_length=255)
    user_type = models.CharField(max_length=1, choices=TYPES_PROF)
    avatar = models.ImageField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(blank=True, max_length=255)


    REQUIRED_FIELDS = ['first_name']
