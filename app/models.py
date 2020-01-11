from django.db import models
from PIL import Image
import datetime as dt
# from django.contrib.auth import User

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=50)
  project_image = models.ImageField(upload_to='projects/')
  description = models.CharField(max_length=400)
  project_link = models.CharField(max_length=70)
  date=models.DateTimeField(auto_now_add=True)
  


  def __str__(self):
    return self.title

  @classmethod
  def all_projects(cls):
    projects = cls.objects.all()
    return projects


class Profile(models.Model):
  name = models.CharField(max_length=70)
  email = models.EmailField(null=True)
  bio=models.CharField(max_length=400)
  profile_image = models.ImageField(upload_to='profile/',null=True)
  # username = models.OneToOneField(User,on_delete=models.CASCADE)
  

  def __str__(self):
    return self.name


  @classmethod
  def all_profiles(cls):
    profiles = cls.objects.all()
    return profiles


