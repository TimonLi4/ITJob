from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=255, verbose_name='Специальность')
    slug=models.SlugField(max_length=255,unique=True,db_index=True,default='',verbose_name='URL')
    description = models.TextField(blank=True,verbose_name='Описание')
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    specification = models.ForeignKey('Specification',on_delete= models.PROTECT,verbose_name='Квалификация')
    tags = models.ForeignKey('Experience',null=True,on_delete= models.PROTECT,related_name='tags',verbose_name='Опыт работы')
    author = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,related_name='posts',null=True,default=None)
    
    #is_pudlished

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('job',kwargs={'job_slug':self.slug})


class Specification(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('specification',kwargs={'spc_slug':self.slug})

class Experience(models.Model):
    exp=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.exp
    
    def get_absolute_url(self):
        return reverse('test',kwargs={'exp_slug':self.slug})

