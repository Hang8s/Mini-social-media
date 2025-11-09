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
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    
