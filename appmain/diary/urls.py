from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),  # URL for the user's dashboard
    path('add/', views.add_entry, name='add_entry'),  # URL to add a new diary entry
    path('view/', views.view_entries, name='view_entries'),  # URL to view all entries
    path('view/<int:entry_id>/', views.view_entry, name='view_entry'),  # URL to view a specific entry by its ID
    path('edit/<int:entry_id>/', views.edit_entry, name='edit_entry'),  # URL to edit a specific entry by its ID
    path('delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),  # URL to delete a specific entry by its ID
    path('login/', auth_views.LoginView.as_view(), name='login'),  # URL for login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL for logout
    path('signup/', views.signup, name='signup'),  # URL for user registration
]
