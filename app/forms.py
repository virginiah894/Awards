from .models import Profile,Project
from django.contrib.auth.models import User
from django  import forms
from crispy_forms.helper import FormHelper
from  crispy_forms.layout import Submit,Layout,Field




class  UserProjectForm(forms.ModelForm):
  helper =FormHelper()
  helper.form_method ='POST'
  helper.add_input(Submit('Post','Post',css_class='btn-primary'))
  class Meta:
     model = Project
     fields =[
       'title',
       'project_image',
       'description',
       'project_link',
       
     ]
  



class AccountUpdate(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']


class DetailsUpdate(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['profile_image','bio']  
