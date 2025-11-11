from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.\
@login_required
def home_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})

@login_required

def detail_view(request):
    pass

@login_required
def create_post(request):
    form = post_creation_form()
    if request.method == 'POST':
        form = post_creation_form(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.save()
            return redirect('home')
    return render(request,'posts/create_post.html',{'form':form})