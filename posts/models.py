from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import os
# Create your models here.

def image_upload_path(instance, filename):
    name, ext = os.path.splitext(filename)
    return f"posts/images/{slugify(name)}{ext}"

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='posts',null=True)
    title = models.CharField(max_length=20)
    body = models.TextField(max_length=2000,blank=True,null=True)
    image = models.ImageField(upload_to=image_upload_path, blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    
class Comments(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.SET_NULL,null=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='comments',null=True)
    body = models.CharField(max_length=256)
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

