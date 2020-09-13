# Imports
from django import forms
from django.core import validators

class FormArticle(forms.Form):
    title = forms.CharField(
        label = "Titulo",
        max_length = 20,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Ingresa el titulo',
                'class': 'form-control'
            }
        ),
        validators = [
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñÑ ]*$', message='El titulo esta mal formado', code='invalid_title')
        ]
    )

    content = forms.CharField(
        label = "Contenido",
        max_length = 100,
        required = True,
        widget = forms.Textarea(
            attrs = {
                'placeholder': 'Ingresa el contenido',
                'class': 'form-control'
            }
        ),
        validators = [
            validators.MaxLengthValidator(20, 'Has puesto demasiado texto')
        ]
    )

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]
    public = forms.TypedChoiceField(
        label = "Publicado",
        choices = public_options,
        widget = forms.Select(
            attrs = {
                'class': 'form-control'
            }
        )
    )