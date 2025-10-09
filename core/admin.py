from django.contrib import admin
from .models import User,Project,Comment,Category,Role,Reply

# Register your models here.
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Role)
admin.site.register(Reply)
