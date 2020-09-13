from django.contrib import admin

# Imports
from .models import Article, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "upgrade_at")

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)