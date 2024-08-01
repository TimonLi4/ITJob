from django.db import models
from django.urls import reverse

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=255, verbose_name='Специальность')
    slug=models.SlugField(max_length=255,unique=False,db_index=True,default='',verbose_name='URL')
    description = models.TextField(blank=True,verbose_name='Описание')
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    #is_pudlished

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('job',kwargs={'job_slug':self.slug})
 