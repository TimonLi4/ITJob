from django.contrib import admin
from .models import Job,Specification,Experience

# Register your models here.

@admin.register(Job)
class AdminJob(admin.ModelAdmin):
    list_display=('id','title','specification','tags')
    list_display_links=('id','title','specification','tags')

@admin.register(Specification)
class AdminSpecification(admin.ModelAdmin):
    list_display=('id','name')
    list_display_links=('id','name')
    
@admin.register(Experience)
class AdminExperience(admin.ModelAdmin):
    list_display=('id','exp')
    list_display_links=('id','exp')