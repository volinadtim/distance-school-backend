from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .serializers import UserSerializer
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'password', 'email',
                    'first_name', 'middle_name', 'last_name',
                    'phone', 'avatar']


admin.site.register(User, CustomUserAdmin)
