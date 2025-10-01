from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Project, Category
from .forms import UploadProjectForm, SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    project_details = Project.objects.all()
    return render(request, 'index.html', {'project_details' : project_details})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            messages.error(request, 'An Error Occured. Try Again!!')
    else:
        form=SignupForm()
    return render(request, 'signup.html', {'form':form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('home')
        else: messages.error(request, "Invalid username or password!!")
    return render(request, 'signin.html')

@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadProjectForm(request.POST,request.FILES)
        if form.is_valid():
            Project = form.save(commit=False)
            Project.uploaded_by = request.user
            Project.save()
            messages.success(request, 'Project Uploaded!!')
            return redirect ('/upload/')
        else:
            messages.error(request, 'An Error Occured. Try Again!!')
    else:
        form = UploadProjectForm()
    return render(request, 'upload.html', { 'form': form})

@login_required
def find(request):
    return render(request, 'find.html')

def welcome(request):
    project_details = Project.objects.all()
    return render(request, 'welcome.html', {'project_details' : project_details})

def project_details(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'project-details.html', {'project' : project})