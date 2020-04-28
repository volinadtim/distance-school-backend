from django.contrib import admin
from .models import Schedule, Subject


class ScheduleAdmin(admin.ModelAdmin):
    model = Schedule
    list_display = ['classes_start']


class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    list_display = ['title']


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Schedule, ScheduleAdmin)
