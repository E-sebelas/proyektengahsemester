from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    book_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    author = models.CharField(max_length=100)