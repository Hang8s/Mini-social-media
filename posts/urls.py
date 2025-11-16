from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
    path('', home_view,name='home'),
    path('post/<int:pk>', detail_view,name='post_detail'),
    path('create_post/', create_post,name='create_post'),
    path('delete_post/<int:pk>', delete_post,name='delete_post'),
    path('like_post/<int:pk>', like_post,name='like_post'),
    path('comments/<int:pk>', comments_view,name='comments'),
]
