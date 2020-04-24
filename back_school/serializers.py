from .models import CustomUser
from rest_framework import routers, serializers, viewsets
from rest_framework.validators import UniqueValidator


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'password', 'username', 'email',
                  'first_name', 'middle_name', 'surname',
                  'phone', 'birthday', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'])
        user.save()
        return user