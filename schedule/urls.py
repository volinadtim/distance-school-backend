from django.urls import path
from .views import ScheduleList, ScheduleDetail, SubjectList

urlpatterns = [
    path('', ScheduleList.as_view()),
    path('<int:pk>/', ScheduleDetail.as_view()),
    path('subjects/', SubjectList.as_view()),
]
