from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

path('',views.home,name='home'),
path('search/',views.search_results,name='search_results'),
path('project/<int:id>/',views.single_project,name ='singleProject'),
path('accounts/profile/', views.profile , name = 'profile'),
path('profile_update/',views.profile_update,name='update'),
path('new_project/<int:id>/',views.add_project,name='newProject'),


]

if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)