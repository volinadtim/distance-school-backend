from .models import CustomUser
from rest_framework import routers, serializers, viewsets


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'password', 'username', 'email',
                  'first_name', 'middle_name', 'surname',
                  'phone', 'birthday', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            name=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
