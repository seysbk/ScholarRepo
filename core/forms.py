from django import forms
from django.forms import ModelForm
from .models import Project,User
from django.contrib.auth.forms import UserCreationForm


class UploadProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','category','cover_image','demo_video','github_link','live_link']

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1','password2']

class UserInfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','bio','github', 'linkedin', 'instagram', 'link', 'profile_pic']
