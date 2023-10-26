from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from appmain.models import Book
from django.http import HttpResponse
from django.core import serializers

def get_books(request):
    data=Book.objects.all()
    return HttpResponse(serializers.serialize("json",data),
    content_type="application/json")

def read(request):
    books =  Book.objects.all()

    context = {
        'products': books,
    }

    return render(request, "read.html", context)

@login_required(login_url='/login')
def favorite(request):
    return 0