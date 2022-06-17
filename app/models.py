
from django.db import models
from cloudinary.models import CloudinaryField
# from django.contrib import admin as Admin

# Create your models here.
class NeighbourHood(models.Model):
    neighbourhood_name=models.CharField(max_length=100,blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)
    Occupants_Count=models.IntegerField(blank=True,null=True)
    # admin=models.ForeignKey(Admin, on_delete=models.CASCADE, related_name="neigborhood",null=True,blank=True)

class User(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    username=models.CharField(max_length=100,blank=True,null=True)
    neighborhood_id=models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name="neigborhood",null=True,blank=True)
    email_user=models.EmailField(max_length=100,blank=True,null=True)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    email=models.EmailField(max_length=100,blank=True,null=True)
    fullname=models.CharField(max_length=100,blank=True,null=True)
    proc_img=CloudinaryField('image',blank=True)
    bio=models.TextField(blank=True,null=True)
    contacts=models.CharField(max_length=200)
    locations=models.CharField(max_length=200)


class Business(models.Model):
    business_name=models.EmailField(max_length=100,blank=True,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="users",null=True,blank=True)
    neighbourhood_id=models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name="neighbourhoods",null=True,blank=True)
    business_email=models.EmailField(max_length=100,blank=True,null=True)


class Post(models.Model):
    title=models.CharField(max_length=100,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts",null=True,blank=True)
    url = models.URLField(max_length=255,null=True,blank=True)
    technologies = models.CharField(max_length=200, blank=True)
    post_img=CloudinaryField('post_img')
    description=models.TextField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)

