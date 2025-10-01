from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signup/' ,views.signup, name='signup'),
    path('home/', views.home, name = 'home'),
    path('signin/', views.signin, name= 'signin'),
    path('upload/', views.upload, name='upload'),
    path('find/', views.find, name='find'),
    path('project/<int:id>/', views.project_details, name = 'project-details'),
]