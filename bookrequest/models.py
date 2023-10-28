from django.db import models


# Create your models here.
class Reqbook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published = models.IntegerField()