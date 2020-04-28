from django.db import models
from accounts.models import Grade, User


class Task(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    deadline = models.DateTimeField(null=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class TaskAnswer(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="answers")


class Attachment(models.Model):
    file = models.FileField(upload_to="files")
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="attachments")
