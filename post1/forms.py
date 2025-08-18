from django import forms
from .models import postdb
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class postform(forms.ModelForm):
    class Meta:
        model = postdb
        fields = ['images','description']


class userregisterform(UserCreationForm):
    
        email = forms.EmailField()
        class Meta:
             model = User
             fields = ('username','email','password1','password2')