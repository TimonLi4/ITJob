from django.urls import path,include
from .views import *
urlpatterns = [
    path('',main_page,name='home'),
    path('about/',about,name='about'),
    path('add_job/',add_job,name='addjob'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('post/<slug:job_slug>/',show_job,name='job'),
    path('specification/<slug:spc_slug>/',show_specification,name='specification'),
    path('test/<slug:exp_slug>/',test,name='test')
]