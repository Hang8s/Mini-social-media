from django.db import models
from django.contrib.auth.models import User

def image_upload_page():
    pass
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    avatar = models.ImageField(upload_to=image_upload_page(),blank=True,null=True)
    bio = models.TextField(null=True,blank=True)