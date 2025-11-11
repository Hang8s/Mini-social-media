from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
    path('', home_view,name='home'),
    path('post/<int:pk>', detail_view,name='post_detail'),
    path('create_post/', create_post,name='create_post'),
]
