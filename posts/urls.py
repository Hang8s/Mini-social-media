from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
    path('', home_view,name='home'),
    path('post/<int:pk>', detail_view,name='post_detail'),
    path('create_post/', create_post,name='create_post'),
    path('delete_post/<int:pk>', delete_post,name='delete_post'),
    path('edit_post/<int:pk>', edit_post,name='edit_post'),
    path('like_post/<int:pk>', like_post,name='like_post'),
    path('like_comment/<int:pk>', like_comment,name='like_comment'),
    path('comments/<int:pk>', comments_view,name='comments'),
    path('delete_comment/<int:pk>/',delete_comment,name='delete_comment')
]
