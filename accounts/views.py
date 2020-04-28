from rest_framework import filters
from django.contrib.auth import get_user_model
from rest_framework import permissions, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, StudentSerializer, TeacherSerializer, AdminSerializer, ParentSerializer, CustomTokenObtainPairSerializer, SchoolSerializer,  GradeSerializer
from .models import Student, Teacher, Admin, Parent, School, Grade
from .permissions import IsStudent, IsTeacher, IsDirector, IsParent, ReadOnly, IsSelf, IsDirectorOwner, IsAdmin

USER = get_user_model()


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserList(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed.
    """
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'middle_name']

    def get_queryset(self):
        queryset = USER.objects.all()
        user_type = self.request.query_params.get('user_type', None)
        if user_type is not None:
            queryset = queryset.filter(user_type=user_type)
        return queryset


class StudentList(generics.ListAPIView):
    """
    API endpoint that allows Students to be viewed.
    """
    permission_classes = [AllowAny]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class TeacherList(generics.ListAPIView):
    """
    API endpoint that allows Teachers to be viewed.
    """
    permission_classes = [AllowAny]
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class UserDetail(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows user to be viewed or edited.
    """
    permission_classes = [IsSelf | IsAdmin | IsDirectorOwner]
    serializer_class = UserSerializer
    queryset = USER.objects.all()


class StudentDetail(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows Student to be viewed or edited.
    """
    permission_classes = [IsSelf | IsAdmin | IsDirectorOwner]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class TeacherDetail(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows Teacher to be viewed or edited.
    """
    permission_classes = [IsSelf | IsAdmin | IsDirectorOwner]
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class UpdateAvatar(APIView):
    def post(self, request, pk):
        user = USER.objects.get(id=pk)
        if (not user):
            return Response(None, status=404)
        user.avatar = request.FILES.get('avatar')
        return Response(user.avatar)


class RegistrationView(generics.CreateAPIView):
    """
    API endpoint that allows record a new User.
    """
    model = USER()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class StudentRecordView(generics.CreateAPIView):
    """
    API endpoint that allows record a new Student.
    """
    model = Student()
    permission_classes = [AllowAny]
    serializer_class = StudentSerializer


class TeacherRecordView(generics.CreateAPIView):
    """
    API endpoint that allows record a new Teacher.
    """
    model = Teacher()
    permission_classes = [AllowAny]
    serializer_class = TeacherSerializer


class ParentRecordView(generics.CreateAPIView):
    """
    API endpoint that allows record a new Parent.
    """
    model = Parent()
    permission_classes = [AllowAny]
    serializer_class = ParentSerializer


class AdminRecordView(generics.CreateAPIView):
    """
    API endpoint that allows record a new Admin.
    """
    model = Admin()
    permission_classes = [AllowAny]
    serializer_class = AdminSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@api_view(['get'])
@permission_classes([AllowAny])
def check_username(request, username):
    return Response({'exists': USER.objects.filter(username__iexact=username).exists()})


class SchoolList(generics.ListCreateAPIView):
    permission_classes = [ReadOnly | IsDirector | IsAdmin]
    serializer_class = SchoolSerializer
    queryset = School.objects.all()


class SchoolDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [ReadOnly | IsDirector | IsAdmin]
    serializer_class = SchoolSerializer
    queryset = School.objects.all()


class GradeList(generics.ListCreateAPIView):
    permission_classes = [ReadOnly | IsDirector | IsAdmin]
    serializer_class = GradeSerializer

    def get_queryset(self):
        school = self.request.query_params.get('school', None)
        if school is not None:
            return Grade.objects.filter(school=school)
        return Grade.objects.all()


class GradeDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [ReadOnly | IsDirector | IsAdmin]
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()
