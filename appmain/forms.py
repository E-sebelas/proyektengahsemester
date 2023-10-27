from django import forms
from django.contrib.auth.forms import UserCreationForm

class AdminRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    admin_code = forms.CharField(max_length=10, required=True)
