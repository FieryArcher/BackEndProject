from django.contrib import admin

from .models import Task
from .models import Story

admin.site.register(Task)
admin.site.register(Story)
