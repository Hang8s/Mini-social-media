from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.\
def home_view(request):
    posts = Post.objects.all()
    user = request.user
    
    search = request.GET.get('search', '')
    
    if search:
        posts = Post.objects.filter(title__icontains=search)
        
    if request.htmx:
        data =  {
        'posts': posts,
        'user':user
        }
        return render(request, 'snippets/posts.html',data)
    
    
    data =  {
        'posts': posts,
        'user':user
        }
    
    return render(request, 'posts/home.html',data)



    

@login_required
def detail_view(request,pk):
    post = get_object_or_404(Post,pk=pk)
    form = comment_form()
    
    data = {
        'post':post,
        'form':form,
        'comments':post.comments.all()
    }
    return render(request,'posts/post_detail.html',data)

@login_required
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.save()
            return redirect('home')
    return render(request,'posts/create_post.html',{'form':form})

@login_required
def edit_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.user != post.author:
        return redirect('home')
    
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)

    form = PostForm(instance=post)
    data = {
        'form':form
    }
    return render(request,'posts/create_post.html',data)
        

@login_required
def delete_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    
    if request.user == post.author:
        if request.method == 'POST':
            post.delete()
            return redirect('home')
            
        return render(request,'posts/delete_post.html')

@login_required
def like_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        
    return render(request,'snippets/likes.html',{'post':post})


@login_required
def like_comment(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
        
    return render(request,'snippets/comments_likes.html',{'comment':comment})   
    
@login_required
def comments_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = comment_form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            return render(
                request,
                "snippets/comments.html",
                {"comments": post.comments.all()}
                )

@login_required 
def delete_comment(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    post = get_object_or_404(Post, pk=comment.post.id)

    if comment.author == request.user:
        comment.delete()
        
    return render(
            request,
            "snippets/comments.html",
            {"comments": post.comments.all()}
            )