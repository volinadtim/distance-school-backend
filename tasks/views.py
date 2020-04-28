from rest_framework import generics, permissions
from accounts.permissions import IsTeacher
from .models import Task, Attachment
from .seializers import TaskSerializer, AttachmentSerializer

from accounts.permissions import ReadOnly, IsTeacher, IsStudent


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [ReadOnly | IsTeacher]

    def get_queryset(self):
        grade = self.request.query_params.get('grade', None)
        if grade is not None:
            return Task.objects.filter(grade=grade)
        return Task.objects.all()


class TaskDetail(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [ReadOnly | IsTeacher]


class AttachmentList(generics.ListCreateAPIView):
    serializer_class = AttachmentSerializer
    permission_classes = [ReadOnly | IsTeacher]
    queryset = Attachment.objects.all()
