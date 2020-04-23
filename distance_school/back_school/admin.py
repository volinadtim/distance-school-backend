from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .serializers import CustomUserSerializer
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'password', 'email',
                    'first_name', 'middle_name', 'surname',
                    'phone', 'avatar']


admin.site.register(CustomUser, CustomUserAdmin)