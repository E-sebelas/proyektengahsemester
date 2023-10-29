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
from appmain.models import Book
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
   
from appmain.models import Post

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
                return redirect('login')  # Ganti dengan halaman pemberitahuan bahwa pendaftaran berhasil
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
            return redirect('login')  # Ganti dengan halaman dashboard pengguna
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
            return redirect('show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('login'))
    return response

def get_books(request):
    data=Book.objects.all()
    return HttpResponse(serializers.serialize("json",data),
    content_type="application/json")

from django.shortcuts import render

def admin_menu(request):
    # Tambahkan logika yang diperlukan untuk halaman admin menu di sini
    return render(request, 'admin_menu.html')


def forum(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'forum.html', context)



def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        book_name = request.POST.get('book_name')
        rating = request.POST.get('rating')
        author = request.POST.get('author')
        
        
        new_post = Post(title=title, content=content, book_name=book_name, rating=rating, author=author)
        new_post.save()
        success = 'Post created successfully'
        return HttpResponse(success)
        

    
"""
class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False"""


def forum_about(request):
    return render(request, 'forum_about.html', {'title': 'About'})
    
# Create your views here.
