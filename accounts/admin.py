from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .serializers import UserSerializer
from .models import User, School


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'password', 'email',
                    'first_name', 'middle_name', 'last_name',
                    'phone', 'avatar']


class SchoolAdmin(admin.ModelAdmin):
    model = School
    list_display = ['full_name', 'short_name']


admin.site.register(School, SchoolAdmin)
admin.site.register(User, CustomUserAdmin)
