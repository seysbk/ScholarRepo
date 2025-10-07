from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField ('User Role', max_length=8)
    permisions = models.CharField()

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role= models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank= True)
    created_at = models.DateTimeField(auto_now_add=True)
    github = models.TextField(null=True, blank=True)
    linkedin = models.TextField(null=True, blank=True)
    instagram = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', null=True, blank=True, default='profile_pic/logo.png')
    
    def __str__(self):
        return self.username
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='project_images/')
    demo_video = models.FileField( blank=True, null=True, upload_to='demo_videos/', default='demo_videos/default.mp4')
    github_link = models.URLField()
    live_link = models.URLField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    assigned_lecturer = models.CharField( max_length=100, blank=True)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #likes counter
    def number_of_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)