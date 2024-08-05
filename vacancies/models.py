from django.db import models
from django.urls import reverse

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=255, verbose_name='Специальность')
    slug=models.SlugField(max_length=255,unique=True,db_index=True,default='',verbose_name='URL')
    description = models.TextField(blank=True,verbose_name='Описание')
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    specification = models.ForeignKey('Specification',on_delete= models.PROTECT)
    
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

