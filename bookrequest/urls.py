from django.urls import path

from . import views

app_name = 'bookrequest'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('get-reqs/', views.get_reqs_json, name='get_reqs_json'),
    path('add-reqs-ajax', views.add_reqs_ajax, name='add_reqs_ajax'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('get-product/', views.get_product_json, name='get_product_json'),
    path('create-product-ajax/', views.add_reqs_ajax, name='add_product_ajax')
]
