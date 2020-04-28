from django.urls import path
from .views import TaskDetail, TaskList, AttachmentList


urlpatterns = [
    path('', TaskList.as_view()),
    path('<int:pk>/', TaskDetail.as_view()),
    path('<int:pk>/attachments/', AttachmentList.as_view())
]
