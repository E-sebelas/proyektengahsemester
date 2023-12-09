import datetime
import json

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect, JsonResponse)
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from forums.forms import CreatePostForm
from forums.models import Post

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json





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

def show_json(request):
    data = Post.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
@require_POST
def add_request_ajax(request):
    try:
        data = json.loads(request.body)
        post = Post(
            title=data["title"],
            content=data["content"],
            book_name=data["book_name"],
            rating=data["rating"],
            author=data["author"],
        )
        post.save()
        return JsonResponse({"message": "Post created successfully"}, status=201)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except KeyError as e:
        return JsonResponse({"error": f"Missing field: {e}"}, status=400)


@login_required    
def show_forum(request):
    # Fungsi ini akan merender halaman main.html dan mengembalikannya sebagai respons.
    return render(request, 'forum.html')

