from django.urls import path

from bookrequest.views import show_main

app_name='bookrequest'

urlpatterns = [
    path('',show_main, name="show_main"),
]