from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import AdminRegistrationForm
from django.http import HttpResponseRedirect
from appmain.models import Book
from django.http import HttpResponse
from django.core import serializers
from appmain.models import Book, Favorite
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse



def show_main(request):
    # Fungsi ini akan merender halaman main.html dan mengembalikannya sebagai respons.
    return render(request, 'main.html')

# View untuk pendaftaran admin
def admin_register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            # Periksa kode verifikasi admin di sini
            admin_code = form.cleaned_data['admin_code']
            if admin_code == 'E-sebelas':  # Ganti dengan kode verifikasi yang Anda tentukan
                user = form.save(commit=False)  # Tambahkan commit=False untuk menghindari penyimpanan langsung ke database
                user.is_staff = True  # Menandai akun sebagai admin
                user.save()  # Simpan akun dengan is_staff yang ditandai
                response = HttpResponseRedirect(reverse('appmain:login'))
                return response
            else:
                # Kode verifikasi tidak valid, tampilkan pesan kesalahan
                form.add_error('admin_code', 'Kode verifikasi tidak valid.')
    else:
        form = AdminRegistrationForm()
    return render(request, 'registration_admin.html', {'form': form})


# View untuk pendaftaran pengguna (user)
def user_register(request):
    if request.method == 'POST':
        # Formulir pendaftaran pengguna
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Proses pendaftaran pengguna di sini
            form.save()
            response = HttpResponseRedirect(reverse('appmain:login'))
            return response
    else:
        form = UserCreationForm()
    return render(request, 'registration_user.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user_logged_in'] = True
            request.session['username'] = user.username
            request.session['is_admin'] = user.is_staff  # Sesuaikan sesuai logika Anda
            return redirect('appmain:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('appmain:login'))
    return response

def get_books(request):
    data=Book.objects.all()
    return HttpResponse(serializers.serialize("json",data),
    content_type="application/json")

def get_books_json(request):
    data=Book.objects.all()
    return HttpResponse(serializers.serialize("json",data))

def admin_menu(request):
    # Tambahkan logika yang diperlukan untuk halaman admin menu di sini
    return render(request, 'admin_menu.html')

def show_favorite(request):
    # Fungsi ini akan merender halaman main.html dan mengembalikannya sebagai respons.
    return render(request, 'favorites.html')

@csrf_exempt
def favorite(request):
    if request.method == 'POST':
        Title = request.POST.get("Title")
        user = request.user

        new_product = Favorite(user=user, Title=Title)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', favorites))

# Create your views here.
