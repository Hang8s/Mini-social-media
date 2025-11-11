from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.\
@login_required
def home_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})

@login_required
def detail_view(request,pk):
    post = get_object_or_404(Post,pk=pk)
    form = comment_form()
    
    if request.method == 'POST':
        form = comment_form(request.POST)
        if form.is_valid():
            comment =form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
            
    data = {
        'post':post,
        'form':form,
        'comments':post.comments.all()
    }
    return render(request,'posts/post_detail.html',data)

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

@login_required
def delete_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    
    if request.user == post.author:
        if request.method == 'POST':
            post.delete()
            return redirect('home')
            
        return render(request,'posts/delete_post.html')
    

    