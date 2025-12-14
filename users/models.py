from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import os


def image_upload_path(instance, filename):
    name, ext = os.path.splitext(filename)
    return f"profile/images/{slugify(name)}{ext}"

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    username = models.CharField(max_length=128,blank=True,null=True)
    avatar = models.ImageField(upload_to=image_upload_path,blank=True,null=True)
    bio = models.TextField(null=True,blank=True)