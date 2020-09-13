from django import forms

class FormArticle(forms.Form):
    title = forms.CharField(
        label = "Titulo"
    )

    content = forms.CharField(
        label = "Contenido"
    )

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]
    public = forms.TypedChoiceField(
        label = "Publicado",
        choices = public_options
    )