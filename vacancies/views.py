from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import *
from .forms import *
# Create your views here.

menu=[
    {'title': 'О сайте', 'url_name':'about'},
    {'title': 'Добавить работу', 'url_name':'addjob'},
    {'title': 'Обратная связь', 'url_name':'contact'},
    {'title': 'Войти', 'url_name':'login'},
]

"""cats_db=[
    {'id':1,'name':'Data Science'},
    {'id':2,'name':'Backend'},
    {'id':3,'name':'Frontend'},
    {'id':4,'name':'GameDev'},
]
"""
def main_page(request):
    jobs = Job.objects.all().order_by('-time_create')

    data={
        'jobs':jobs,
        'menu':menu,
        'cat_selected':0,
    }

    return render(request,'vacancies/main.html',data)

def about(request):
    return HttpResponse('<h1>О сайте</h1>')

def add_job(request):
    if request.method == 'POST':
        form = AddJob(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddJob()
    data = {
        'menu':menu,
        'title': 'Добавить вакансию',
        'form': form,
    }
    return render(request,'vacancies/addjob.html',data)



def contact(request):
    return HttpResponse('<h1>Обратная связь</h1>')

def login(request):
    return HttpResponse('<h1>Авторизация</h1>')

def show_job(request,job_slug):
    post = get_object_or_404(Job,slug = job_slug)
    data={
        'title':post.title,
        'menu':menu,
        "post":post,
        #'category':cats_db
    }
    return render(request,'vacancies/job.html',data)

def show_specification(request,spc_slug):
    specification_d = get_object_or_404(Specification,slug=spc_slug)
    jobs = Job.objects.filter(specification_id=specification_d.pk)
    data={
        'title': f'Спецификация: {specification_d.name}',
        'jobs':jobs,
        'menu':menu,
        'cat_selected':specification_d.pk,
    }

    return render(request,'vacancies/main.html',data)