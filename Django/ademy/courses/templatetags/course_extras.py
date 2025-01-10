from django import template
from django.utils.safestring import mark_safe
from courses.models import Course

import markdown2

register = template.Library()

@register.simple_tag
def last_course():
    '''Obtiene el ultimo curso puesto en la libreria'''
    return Course.objects.latest('created_at')

@register.filter('time_estimate')
def time_estimate(word_count):
    '''Estima el tiempo de lectura de un texto en minutos'''
    minutes = round(word_count/20)
    return minutes

@register.filter('markdown_to_html')
def markdown2_to_html(markdown_text):
    '''Convierte markdown en html'''
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)