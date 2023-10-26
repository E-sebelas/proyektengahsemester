from django.contrib import admin
from django.urls import path, include
from appmain.views import get_books, read

app_name="appmain"

urlpatterns = [
    path("get_books/",get_books, name="get_books"),
    path("read/",read, name="read"),
]
