from django import forms
from .models import *


class AddJob(forms.ModelForm):


    class Meta:
        model = Job
        fields=['title','slug','description']