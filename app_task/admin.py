from django.contrib import admin
from .models import Task, TestingTask

admin.site.register(Task)
admin.site.register(TestingTask)
