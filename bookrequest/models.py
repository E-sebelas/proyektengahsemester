from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Reqbook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published = models.IntegerField()