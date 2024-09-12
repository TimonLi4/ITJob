from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddJobForm
# Create your views here.

menu=[
    {'title': 'О сайте', 'url_name':'about'},
    {'title': 'Добавить работу', 'url_name':'addjob'},
    {'title': 'Обратная связь', 'url_name':'contact'},
    #{'title': 'Войти', 'url_name':'login'},
]

"""cats_db=[
    {'id':1,'name':'Data Science'},
    {'id':2,'name':'Backend'},
    {'id':3,'name':'Frontend'},
    {'id':4,'name':'GameDev'},
]
"""

items = Specification.objects.order_by('id').values('id','name')


def main_page(request):
    jobs = Job.objects.all().order_by('-time_create')

    data={
        'jobs':jobs,
        'menu':menu,
        'cat_selected':0,
    }

    return render(request,'vacancies/main.html',data)

@login_required
def about(request):
    return HttpResponse('<h1>О сайте</h1>')
"""
@login_required
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
"""
"""
class AddJob(View):
    def get(self,request):
        form = AddJobForm()
        data={
            'title':'Добавление статьи',
            'form': form
        }
        return render(request,'vacancies/addjob.html',data)
    

    def post(self,request):
        form = AddJobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request,'vacancies/addjob.html',{'title': 'Добавление статьи', 'form': form})"""

class AddJob(LoginRequiredMixin,FormView):
    form_class = AddJobForm
    template_name='vacancies/addjob.html'
    success_url= reverse_lazy('home')
    extra_context={
        'menu':menu,
        'title':'Добавление Вакансии',
    }

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        w.save()
        return super().form_valid(form)
    """def form_valid(self,form):
        form.save()
        return super().form_valid(form)"""


def checkbox(request,name):
    if request.method == 'POST':
        checkbox_states = []
        for item in items:
            checkbox_name = f'{name}{item["id"]}'
            if checkbox_name in request.POST:
                checkbox_states.append(item["id"])
            
        return checkbox_states


def sorting(request):
    #check = request.POST.getlist('checkid')
    
    checkbox_states = checkbox(request,'checkbox_')
    checkbox_tags = checkbox(request,'tags_')
    jobs = Job.objects.all()
    
    if len(checkbox_states) > 0:
        jobs = jobs.filter(specification_id__in=checkbox_states)

    if len(checkbox_tags) > 0:
        jobs = jobs.filter(tags_id__in= checkbox_tags)
    return render(request,'vacancies/main.html',{'jobs': jobs})

    


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


def exp(request,exp_slug):
    experience= get_object_or_404(Experience,slug = exp_slug)
    jobs =Job.objects.filter(tags_id=experience.id)

    data={
        'title': f'Опыт: {experience.exp}',
        'jobs':jobs,
        'menu':menu,
        'cat_selected':experience.pk,
    }
    return render(request,'vacancies/main.html',data)


def combine(request):
    if request.method == 'POST':
        data = {
        'name':request.POST.get('id_1'),
    }
    else:
        data = {
        'name':'dont work'
    }
    
    return render(request,'vacancies/test.html',data)