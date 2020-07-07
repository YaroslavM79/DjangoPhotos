from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import re
from .models import PictureBlog


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username:',
                               help_text='Username must be a maximum of 150 characters',
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Password:', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Password confirmation:',
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.CharField(label='email:', widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username:', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Password:', widget=forms.PasswordInput(attrs={"class": "form-control"}))

#--------------------
#TODO: Add Form for add picture

# class NewsForm(forms.ModelForm):
#     class Meta:
#         model = PictureBlog
#         fields = '__all__'
#         widgets = {
#         }
