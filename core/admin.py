from django.contrib import admin
from .models import User
from .models import Project
from .models import Comment
from .models import Like
from .models import Category
from .models import Role

# Register your models here.
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Category)
admin.site.register(Role)
