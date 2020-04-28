from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import CustomTokenObtainPairView, RegistrationView, check_username, UserList, UserDetail, StudentRecordView, TeacherRecordView, ParentRecordView, StudentDetail, TeacherDetail, StudentList, TeacherList, UpdateAvatar, SchoolList, SchoolDetail, GradeList, GradeDetail

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegistrationView.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('update-avatar/<int:pk>/', UpdateAvatar.as_view()),
    path('students/', StudentList.as_view()),
    path('teachers/', TeacherList.as_view()),
    # # path('directors/', DirectorList.as_view()),
    path('students/<int:pk>/', StudentDetail.as_view()),
    path('teachers/<int:pk>/', TeacherDetail.as_view()),
    # # path('directors/<int:pk>/', DirectorDetail.as_view()),
    path('check-username/<str:username>/', check_username),
    path('schools/', SchoolList.as_view()),
    path('schools/<int:pk>/', SchoolDetail.as_view()),
    path('classes/', GradeList.as_view()),
    path('school-classes/<int:school>/', GradeList.as_view()),
    path('classes/<int:pk>/', GradeDetail.as_view()),
]
