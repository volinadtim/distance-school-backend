from .models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password']
        extra_kwargs = {'password': {'write_only': True}}
