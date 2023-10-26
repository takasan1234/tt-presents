from django.contrib import admin

from .models import Choice, Question, Sum

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Sum)