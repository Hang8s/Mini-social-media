from django.shortcuts import render , redirect , get_object_or_404
from .forms import *
from django.contrib.auth import authenticate , login , logout
from .models import Profile
from posts.models import Post, Comments

# Create your views here.
def register(request):
    form = user_register_form()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            Profile.objects.create(user=user)
            login(request,user)
            
            return redirect('home')
            
    
    return render(request,'users/register.html',{'form':form})   

def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(username=username, password=password)
            login(request,user)
            
            return redirect('home')
    
    return render(request,'users/login.html',{'form':form})   
    
def user_logout(request):
    logout(request)
    return redirect('users:login')

def profile(request,pk):
    profile = get_object_or_404(Profile,pk=pk)
    user = profile.user
    posts = Post.objects.filter(author = user)
    
    total_likes = user.liked_posts.count()
    total_ccomments = user.comments.count()
    
    content_type = request.GET.get('type')
    
    
    data = {
        'profile':profile,
        'posts':posts,
        'total_likes':total_likes,
        'total_comments':total_ccomments,
    }
    
    if content_type == 'posts':
        return render(request, 'snippets/posts.html', data)
    elif content_type == 'likes':
        data['posts'] = Post.objects.filter(likes = user)
        return render(request, 'snippets/posts.html', data)
    elif content_type == 'comments':
        data['comments'] = Comments.objects.filter(author=user)
        return render(request, 'snippets/comments.html', data)
        
    

 
    return render(request,'users/profile.html',data)

def edit_profile(request,pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.user != profile.user:
        return redirect ('home')
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile',pk=profile.pk)
        
    else:
        form = ProfileForm(instance=profile)
        
        
    data = {
        'profile':profile,
        'form':form
        }
        
    return render(request,'users/edit_profile.html',data)