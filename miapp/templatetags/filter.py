from django import template

register = template.library()

@register.filter(name='saludo')

def saludo(value):
    "texto"|saludo