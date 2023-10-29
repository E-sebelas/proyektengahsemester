from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Book(models.Model):
    Title = models.TextField(null=True, blank=True)
    Author = models.TextField(null=True, blank=True)
    Link = models.URLField(null=True, blank=True)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    book_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    author = models.CharField(max_length=100)



    def __str__(self):
        return self.title
    
    