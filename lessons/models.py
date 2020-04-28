from django.db import models
from schedule.models import ScheduleLesson


class Lesson(models.Model):
    schedule_lesson = models.ForeignKey(
        ScheduleLesson, on_delete=models.CASCADE, related_name="lessons")
    date = models.DateField()
    body = models.TextField()
