from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class user_register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-2 border rounded',
            'placeholder': 'username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-2 border rounded',
            'placeholder': 'password'
        })
    )
