
from django.db import models
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# from django.contrib import admin as Admin

# Create your models here.
class NeighbourHood(models.Model):
    neighbourhood_name=models.CharField(max_length=100,blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)
    Occupants_Count=models.IntegerField(blank=True,null=True)
    # admin=models.ForeignKey(Admin, on_delete=models.CASCADE, related_name="neigborhood",null=True,blank=True)

    def __str__(self):
        return self.neighbourhood_name

# class User(AbstractUser):
#     first_name=models.CharField(max_length=100,blank=True,null=True)
#     last_name=models.CharField(max_length=100,blank=True,null=True)
#     username=models.CharField(max_length=100,blank=True,null=True)
#     neighborhood_id=models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name="neigborhood",null=True,blank=True)
#     email_user=models.EmailField(max_length=100,blank=True,null=True)
#     password=models.CharField(max_length=100,blank=True,null=True)
    
#     def save_user(self):
#         self.save()
        
#     def set_password(self,raw_password):
#         self.password =make_password(raw_password)
#         self._password =raw_password

#     def __str__(self):
#         return self.username

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    fullname=models.CharField(max_length=100,blank=True,null=True)
    username=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    proc_img=CloudinaryField('image',blank=True)
    bio=models.TextField(blank=True,null=True)
    contacts=models.CharField(max_length=200)
    locations=models.CharField(max_length=200)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

  

    def update_profile(self,id,profile):
        updated_profile=Profile.objects.filter(id=id).update(profile)
        return updated_profile

    def __str__(self):
        return self.fullname

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            instance.profile.save()

        post_save.connect(Profile, sender=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        Profile.objects.get_or_create(user=instance)
        instance.profile.save()

class Business(models.Model):
    business_name=models.EmailField(max_length=100,blank=True,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="users",null=True,blank=True)
    neighbourhood_id=models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name="neighbourhoods",null=True,blank=True)
    business_email=models.EmailField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.business_name

class Post(models.Model):
    title=models.CharField(max_length=100,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts",null=True,blank=True)
    post_img=CloudinaryField('post_img')
    description=models.TextField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def save_post(self):
        self.save()

    def __str__(self):
        return self.title