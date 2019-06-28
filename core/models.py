from django.db import models
from datetime import date

# Create your models here.

class Book(models.model):
    title = models.Charfield(max_length=200)
    author = models.Charfield(max_length=100)
    description = models.Charfield(max_length=1000)
    URL = models.URLField(unique=True)
    slug = models.Slugfield(max_length=100)
    date = models.DateTimeField(default=date.today)

    def __str__(self):
        return self.title

class Category(models.model):
    title = models.Charfield(max_length=200)
    slug = models.Slugfield(max_length=100)

    def __str__(self):
        return self.title

