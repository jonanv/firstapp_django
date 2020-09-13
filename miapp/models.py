from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to="articles")
    public = models.BooleanField(verbose_name='Público')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    upgrade_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['-id']

    def __str__(self):
        if self.public:
            publico = "(publicado)"
        else:
            publico = "(privado)"

        return f"{ self.title } { publico }"

class Category(models.Model):
    name = models.CharField(max_length=110, verbose_name='Nombre')
    description = models.CharField(max_length=250, verbose_name='Descripción')
    created_at = models.DateTimeField()

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['-id']