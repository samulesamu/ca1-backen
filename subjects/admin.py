from django.contrib import admin

# Register your models here.

from .models import Subject, Notes

admin.site.register(Subject)
admin.site.register(Notes)