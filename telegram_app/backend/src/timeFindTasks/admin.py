from django.contrib import admin
from . import models


class WordsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'timer', 'word']
    list_editable = ['timer', 'word']


admin.site.register(models.Words, WordsAdmin)
