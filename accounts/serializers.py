from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from .models import Student, Teacher, Admin, Parent, School, Grade

USER = get_user_model()


class UserSerializer(ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = USER.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            user_type=validated_data['user_type'],
        )
        user_type = validated_data['user_type']
        user.set_password(validated_data['password'])
        user.save()
        if user_type == 'S':
            student = Student.objects.create(user=user)
            student.save()
        elif user_type == 'T':
            teacher = Teacher.objects.create(user=user)
            teacher.save()
        elif user_type == 'D':
            director = Teacher.objects.create(user=user, is_director=True)
            director.save()
        elif user_type == 'A':
            admin = Admin.objects.create(user=user)
            admin.save()
        elif user_type == 'P':
            parent = Parent.objects.create(user=user)
            parent.save()
        return user

    class Meta:
        model = USER
        exclude = ['groups', 'is_staff', 'is_superuser',
                   'user_permissions', 'is_active', 'date_joined']


class StudentSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data["user_type"] = "S"
        user = UserSerializer.create(**validated_data)
        student = Student.objects.create(user)
        student.save()
        return student

    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data["user_type"] = "T"
        user = UserSerializer.create(**validated_data)
        teacher = Teacher.objects.create(user)
        teacher.save()
        return teacher

    class Meta:
        model = Teacher
        fields = '__all__'


# class DirectorSerializer(ModelSerializer):

#     def create(self, validated_data):
#         validated_data["user_type"] = "D"
#         user = UserSerializer.create(**validated_data)
#         director = Director.objects.create(user)
#         director.save()
#         return director

#     class Meta:
#         model = Director
#         fields = '__all__'


class ParentSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data["user_type"] = "P"
        user = UserSerializer.create(**validated_data)
        parent = Parent.objects.create(user)
        parent.save()
        return parent

    class Meta:
        model = Parent
        fields = '__all__'


class AdminSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data["user_type"] = "A"
        user = UserSerializer.create(**validated_data)
        admin = Admin.objects.create(user)
        admin.save()
        return admin

    class Meta:
        model = Admin
        fields = '__all__'


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_type'] = user.user_type

        return token

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class SchoolSerializer(ModelSerializer):
    teachers = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        fields = '__all__'
        model = School


class GradeSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Grade
