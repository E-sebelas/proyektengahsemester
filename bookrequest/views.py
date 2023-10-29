import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect)
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from bookrequest.forms import ReqForm
from bookrequest.models import Reqbook


@login_required(login_url='/login')
def show_main(request):
    requests = Reqbook.objects.filter(user=request.user)
    context = {'name': request.user.username,
               'requests': requests,
               'last_login': request.COOKIES.get('last_login', 'Cookie Not Found'),
    }
    return render(request, 'bookreq-main.html', context)


def get_reqs_json(request):
    reqs_item = Reqbook.objects.all()
    return HttpResponse(serializers.serialize('json', reqs_item))

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('bookrequest:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("bookrequest:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('bookrequest:login'))
    response.delete_cookie('last_login')
    return response

def get_product_json(request):
    req_item = Reqbook.objects.all()
    return HttpResponse(serializers.serialize('json', req_item))

@csrf_exempt
def add_reqs_ajax(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        published = request.POST.get("published")
        user = request.user
        
        new_request = Reqbook(title=title,author=author,published=published,user=user)
        new_request.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound

