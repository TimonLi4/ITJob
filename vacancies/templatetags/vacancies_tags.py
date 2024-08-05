from django import template
import vacancies.views as views
from vacancies.models import Specification

register=template.Library()




@register.inclusion_tag('vacancies/list_categories.html')
def show_categories(cat_selected=0):
    cats = Specification.objects.all()
    return {'cats':cats,'cat_selected':cat_selected}
