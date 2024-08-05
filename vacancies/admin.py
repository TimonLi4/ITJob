from django.contrib import admin
from .models import Job,Specification

# Register your models here.

@admin.register(Job)
class AdminJob(admin.ModelAdmin):
    list_display=('id','title')

@admin.register(Specification)
class AdminSpecification(admin.ModelAdmin):
    list_display=('id','name')