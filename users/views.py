from django.shortcuts import render , redirect
from .forms import *
from django.contrib.auth import authenticate , login , logout

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
    return redirect('login')