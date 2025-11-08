from django.shortcuts import render
from .models import *

# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})


def detail_view(request):
    pass