from django.contrib import admin
from django.urls import path , include
from .views import *

app_name ='users'

urlpatterns = [
    path('register/', register,name='register'),
    path('login/', user_login,name='login'),
    path('logout/', user_logout,name='logout'),
    path('profile/<int:pk>/',profile,name='profile'),
    path('edit_profile/<int:pk>/',edit_profile,name='edit_profile'),
]
