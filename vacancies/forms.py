from django import forms
from .models import *


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields=['title','slug','description','specification','tags']


class CheckBox(forms.Form):
    choices = forms.MultipleChoiceField()