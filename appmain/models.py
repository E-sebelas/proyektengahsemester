from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    Title = models.TextField(null=True, blank=True)
    Author = models.TextField(null=True, blank=True)
    Link = models.URLField(null=True, blank=True)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)
