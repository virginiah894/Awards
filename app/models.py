from django.db import models
from PIL import Image
import datetime as dt
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import  post_save

# Create your models here.





class Profile(models.Model):
  name = models.CharField(max_length=70)
  email = models.EmailField(null=True)
  bio = models.CharField(max_length=400)
  profile_image = models.ImageField(upload_to='profile/',null=True, blank=True)
  user= models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)
  

  def __str__(self):
    return self.name


  @classmethod
  def all_profiles(cls):
    profiles = cls.objects.all()
    return profiles



  @receiver(post_save,sender=User)
  def create_profile(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    
  @receiver(post_save,sender=User)
  def save_profile(sender, instance,**kwargs):
    instance.profile.save()
 

class Project(models.Model):
  title = models.CharField(max_length=50)
  project_image = models.ImageField(upload_to='projects/')
  description = models.CharField(max_length=400)
  project_link = models.CharField(max_length=70)
  date=models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
  profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
  


  def __str__(self):
    return self.title

  @classmethod
  def all_projects(cls):
    projects = cls.objects.all()
    return projects
  @classmethod
  def search_by_title(cls,search_term):
    projects = cls.objects.filter(title__icontains=search_term)
    return projects


class Review(models.Model):
    design = models.PositiveIntegerField(default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    review = models.TextField(null=True)
    usability = models.PositiveIntegerField(default=0)
    content = models.PositiveIntegerField(default=0)
    

