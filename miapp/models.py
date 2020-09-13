from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen')
    public = models.BooleanField(verbose_name='Público')
    created_at = models.DateTimeField(auto_now_add=True)
    upgrade_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['-id']

class Category(models.Model):
    name = models.CharField(max_length=110, verbose_name='Nombre')
    description = models.CharField(max_length=250, verbose_name='Descripción')
    created_at = models.DateTimeField()

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['-id']