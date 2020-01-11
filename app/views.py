from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Profile

# Create your views here.
def home(request):
  projects= Project.objects.all()
  return render(request,'index.html',{'projects':projects})

