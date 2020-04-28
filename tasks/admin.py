from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ('body', 'deadline')


admin.site.register(Task, TaskAdmin)
