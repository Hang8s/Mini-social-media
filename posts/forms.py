from django import forms
from .models import Post , Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','image']
        
class comment_form(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['body']