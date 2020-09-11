from django import template

register = template.Library()

@register.filter(name='saludo')
def saludo(value):
    largo = ''
    if len(value) > 8:
        largo = '<p>Tu nombre es muy largo</p>'
        
    return f"<h1 style='background-color: green; color: white'>Bievenido, { value }</h1>" + largo