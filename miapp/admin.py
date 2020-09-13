from django.contrib import admin

# Imports
from .models import Article, Category

# Configurar titulo del panel
title = "Master en Python - Django GVG"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de gestion"

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "upgrade_at")

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)