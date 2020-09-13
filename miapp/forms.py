from django import forms

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
        )
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
        )
    )

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]
    public = forms.TypedChoiceField(
        label = "Publicado",
        choices = public_options
    )