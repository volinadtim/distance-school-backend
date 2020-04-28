from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .models import Schedule, ScheduleDay, ScheduleLesson, Subject
from .serializers import ScheduleSerializer, SubjectSerializer
from accounts.permissions import ReadOnly, IsDirector, IsAdmin


class ScheduleList(ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [ReadOnly | IsDirector]


class ScheduleDetail(RetrieveDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [ReadOnly | IsDirector]


class SubjectList(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [ReadOnly | IsAdmin]
