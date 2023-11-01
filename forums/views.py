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

from forums.forms import CreatePostForm
from forums.models import Post


@login_required(login_url='/login')



def get_request_json(request):
    reqs_item = Post.objects.all()
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
            response = HttpResponseRedirect(reverse("post:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('forum:login'))
    response.delete_cookie('last_login')
    return response

def get_post_json(request):
    req_item = Post.objects.all()
    return HttpResponse(serializers.serialize('json', req_item))

@csrf_exempt
def add_request_ajax(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post =Post(
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"],
                book_name=form.cleaned_data["book_name"],
                rating=form.cleaned_data["rating"],
                author=form.cleaned_data["author"],
                
            )
            post.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound

    
def show_forum(request):
    # Fungsi ini akan merender halaman main.html dan mengembalikannya sebagai respons.
    return render(request, 'forum.html')

