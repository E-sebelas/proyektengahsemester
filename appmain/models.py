from django.db import models

# Create your models here.
class Book(models.Model):
    Title = models.TextField(null=True, blank=True)
    Author = models.TextField(null=True, blank=True)
    Link = models.URLField(null=True, blank=True)
    Bookshelf = models.TextField(null=True, blank=True)