from django.urls import path
from forums.views import show_forum
from forums.views import show_json
from forums.views import create_product_flutter
from . import views

app_name = 'forums'

urlpatterns = [
    
    path('get-request/', views.get_request_json, name='get_request_json'),
    path('add-request-ajax', views.add_request_ajax, name='add_request_ajax'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('get-post/', views.get_post_json, name='get_post_json'),
    path('create-post-ajax/', views.add_request_ajax, name='add_post_ajax'),
    path('show_forum/', show_forum, name='show_forum'),
    path('json/', show_json, name='show_json'),
    path('create-post-json/', views.create_post_json, name='create_post_json'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter')
]
