from django.contrib import admin

# Register your models here.

from .models import Choice, Question, Contact

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Contact)