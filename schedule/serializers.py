from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Schedule, ScheduleDay, ScheduleLesson, Subject


class SubjectSerializer(ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'


class ScheduleSerializer(ModelSerializer):
    days = serializers.StringRelatedField(many=True)

    class Meta:
        model = Schedule
        fields = '__all__'


class ScheduleDaySerializer(ModelSerializer):
    lessons = serializers.StringRelatedField(many=True)
    subject_name = serializers.CharField(source='subject.title')

    class Meta:
        model = ScheduleDay
        fields = '__all__'


class ScheduleLessonSerializer(ModelSerializer):

    class Meta:
        model = ScheduleLesson
        fields = '__all__'
