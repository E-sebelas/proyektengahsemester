from django.urls import path
from django.contrib.auth.views import LoginView
from appmain.views import get_books, create

from . import views

appname="appmain"

from . import views
from django.contrib.auth.views import LoginView
from appmain.views import get_books, get_books_json, favorite, get_favorites, show_favorite

app_name='appmain'

urlpatterns = [
    # URL untuk halaman pendaftaran
    path('', views.show_main, name='show_main'),
    path('login/', views.login_user, name='login'),
    path('adminregister/', views.admin_register, name='admin_register'),
    path('userregister/', views.user_register, name='user_register'),
    path('logout/', views.logout_user, name='logout'),
    path('adminmenu/', views.admin_menu, name='admin_menu'),
    path("get_books/",get_books, name="get_books"),
    path('forum/', views.forum, name='forum-home'),
    path('create/', views.create, name='create'),
    path("get_books_json/",get_books_json, name="get_books_json"),
    path('favorite/', favorite, name='favorite'),
    path('get_favorites/', get_favorites, name='get_favorites'),
    path('show_favorite/', show_favorite, name='show_favorite'),
    # Tambahkan URL lainnya sesuai kebutuhan
    
    # Tambahkan URL lainnya sesuai kebutuhan
]

