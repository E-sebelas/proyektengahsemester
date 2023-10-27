from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    # URL untuk halaman pendaftaran
    path('', views.show_main, name='show_main'),
    path('login/', views.login_user, name='login'),
    path('adminregister/', views.admin_register, name='admin_register'),
    path('userregister/', views.user_register, name='user_register'),
    path('logout/', views.logout_user, name='logout'),
    path('adminmenu/', views.admin_menu, name='admin_menu'),
    # Tambahkan URL lainnya sesuai kebutuhan
]
