from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    public = models.BooleanField()
    created_at = models.DateField(auto_now_add = True)
    upgrade_at = models.DateField(auto_now = True)

class Category(models.Model):
    