from django import template
import vacancies.views as views
from vacancies.views import menu
from vacancies.models import Specification,Experience, Job
from django.db.models import Q

register=template.Library()




@register.inclusion_tag('vacancies/list_categories.html')
def show_categories():
    cats = Specification.objects.all()
    exp = Experience.objects.all()
    return {'cats':cats, 'exp': exp}

@register.simple_tag()
def get_menu():
    return menu



"""@register.inclusion_tag('vacancies/test.html')
def show_exp(exp_selected=0):
    exp = Experience.objects.all()
    return {'exp':exp,'exp_selected':exp_selected}"""


"""@register.inclusion_tag('vacancies/test.html')
def combine(exp_selected=0, cat_selected=0):
    exp = Job.objects.filter(Q(specification_id=cat_selected) & Q(tags_id=exp_selected))
    return {'exp':exp,'exp_selected':exp_selected}"""
