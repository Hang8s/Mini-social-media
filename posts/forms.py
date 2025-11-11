from django import forms
from .models import Post


class post_creation_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','image']