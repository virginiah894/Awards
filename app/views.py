from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project, Profile
from .forms import AccountUpdate, DetailsUpdate,UserProjectForm
from django.contrib import messages

# Create your views here.
def home(request):
  projects= Project.objects.all()
  return render(request,'index.html',{'projects':projects})
def search_results(request):
  if 'project' in request.GET and request.GET['project']:
    search_term = request.GET .get("project")
    searched_projects = Project.search_by_title(search_term)
    message = f'{search_term}'
    return render (request,'search.html',{'message':message,'projects':searched_projects})
  else:
    message = 'Nothing was searched'
    return render(request,'search.html',{'message':message})
def single_project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"project.html", {"project":project})


def profile(request):
  current_user = request.user
  
  profile = Profile.objects.get_or_create(user=request.user)
  images = request.user.project_set.all()
  
  project = images.count()
  
  
  return render(request,'profile.html',{"profile":profile,'images':images,"project":project})

def profile_update(request):
  
  if request.method == 'POST':
       user_form = AccountUpdate(request.POST,instance=request.user)
       details_form = DetailsUpdate(request.POST ,request.FILES,instance=request.user.profile)
       if user_form.is_valid() and details_form.is_valid():
          user_form.save()
          details_form.save()
          messages.success(request,f'Your Profile account has been updated successfully')
          return redirect('profile')
  else:
  

      user_form = AccountUpdate(instance=request.user)
      
      details_form = DetailsUpdate(instance=request.user.profile) 
  forms = {
    'user_form':user_form,
    'details_form':details_form
  }
  return render(request,'profile_update.html',forms)

def add_project(request,id):
    current_user = request.user
    if request.method == 'POST':
        form = UserProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.creator = current_user
            project.save()
        return HttpResponseRedirect('/')

    else:
        form =UserProjectForm
    return render(request, 'new_project.html', {"form": form})

  








