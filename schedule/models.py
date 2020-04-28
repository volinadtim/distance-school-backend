from django.db import models


class Subject(models.Model):
    """
    Subject model
    """
    title = models.CharField(max_length=30)


class Schedule(models.Model):
    classes_start = models.IntegerField(default=540)


class ScheduleDay(models.Model):
    schedule = models.ForeignKey(
        Schedule, on_delete=models.CASCADE, related_name="days")


class ScheduleLesson(models.Model):
    schedule_day = models.ForeignKey(
        ScheduleDay, on_delete=models.CASCADE, related_name="lessons")
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, related_name="schedule_lessons", null=True)
    place = models.PositiveIntegerField()
