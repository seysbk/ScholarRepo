from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Project, Category,Comment,Reply
from .forms import UploadProjectForm, SignupForm,UserInfo,CommentForm,ReplyForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def home(request):
    project_details = Project.objects.all().order_by('-created_at')
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
    if request.method == "POST":
        search = request.POST['search'] #name of the input field / what was typed
        projects = Project.objects.filter( Q(title__contains=search) | Q(category__name__contains=search) | Q(uploaded_by__username__contains=search))
        return render(request, 'find.html', {'search':search, 'projects':projects},)
    else:
        return render(request, 'find.html')

def welcome(request):
    project_details = Project.objects.all().order_by('-created_at')
    return render(request, 'welcome.html', {'project_details' : project_details})

@login_required
def project_details(request, id):
    project = get_object_or_404(Project, pk=id)
    comments = Comment.objects.filter(project=project).order_by('-created_at')
    comment_form = CommentForm()
    reply_form = ReplyForm()
    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.project = project
                comment.user = request.user
                comment.save()
                return redirect('project-details', id=project.id)
        if 'reply_submit' in request.POST:
            reply_form = ReplyForm(request.POST)
            if reply_form.is_valid():
                reply = reply_form.save(commit=False)
                reply.user = request.user
                reply.comment = Comment.objects.get(id=request.POST.get('comment_id'))
                reply.save()
                return redirect('project-details', id=project.id)
    context = {
        'project': project,
        'comments': comments,
        'comment_form': comment_form,
        'reply_form': reply_form,
    }
    return render(request, 'project-details.html', context)


@login_required
def settings_general(request):
    user = request.user
    if request.method == 'POST':
        form = UserInfo(request.POST,request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            User.username = request.user.username
            form.save()
            messages.success(request, 'Profile Updated!!')
            return redirect ('/settings/')
        else:
            messages.error(request, 'An Error Occured. Try Again!!')
            print(form.errors)
    else:
        form = UserInfo(instance=user)
    return render(request, 'settings.html', { 'form': form,'user':user},)

@login_required
def profile(request,id):
    project = get_object_or_404(Project, pk=id)
    user = project.uploaded_by
    projects = Project.objects.filter(uploaded_by=user)
    return render(request, 'profile.html', {'user':user, 'projects':projects},)

@login_required
def like_project(request, id):
    project = get_object_or_404(Project, pk=id)
    if project.likes.filter(id=request.user.id):
        project.likes.remove(request.user)
    else:
        project.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER','/'))

@login_required
def signout(request):
    logout(request)
    return redirect ('welcome')

@login_required
def project_settings(request):
    user = request.user
    projects = Project.objects.filter(uploaded_by=user)
    return render(request, 'project-settings.html', {'user':user, 'projects':projects},)

@login_required
def delete_project(request, id):
    project = Project.objects.get(pk=id)
    project.delete()
    messages.success(request, 'Project Deleted!!')
    return redirect(request.META.get('HTTP_REFERER','/'))

@login_required
def my_profile(request):
    user = request.user
    projects = Project.objects.filter(uploaded_by=user)
    return render(request, 'profile.html', {'user':user, 'projects':projects},)

@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, pk=id)
    if comment.user == request.user:
        comment.delete()
    return redirect(request.META.get('HTTP_REFERER','/'))

@login_required
def delete_reply(request, id):
    reply = get_object_or_404(Reply, pk=id)
    if reply.user == request.user:
        reply.delete()
    return redirect(request.META.get('HTTP_REFERER','/'))

def settings_legal(request):
    return render(request, 'legal.html')