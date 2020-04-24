from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    TYPES_PROF = (
        ('D', 'Director'),
        ('S', 'Student'),
        ('T', 'Teacher'),
        ('P', 'Parent'),
        ('A', 'Admin'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    middle_name = models.CharField(blank=True, max_length=150)
    user_type = models.CharField(max_length=1, choices=TYPES_PROF)
    avatar = models.ImageField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(blank=True, max_length=15)

    REQUIRED_FIELDS = ['first_name', 'last_name']
