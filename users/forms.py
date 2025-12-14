from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile

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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username','avatar', 'bio']
        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'w-full p-2 border rounded'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded',
                'rows': 4
            }),
        }
