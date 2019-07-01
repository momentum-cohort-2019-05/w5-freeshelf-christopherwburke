from django.db import models
from datetime import date

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    URL = models.URLField(unique=True)
    slug = models.SlugField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title

