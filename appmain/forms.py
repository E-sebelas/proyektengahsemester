from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from appmain.models import Favorite

class AdminRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    admin_code = forms.CharField(max_length=10, required=True)

class FavoritesForm(ModelForm):
    class Meta:
        model = Favorite
        fields = ["Title"]



