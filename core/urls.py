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
    path('settings/general', views.settings_general, name = 'settings'),
    path('profile/<int:id>/', views.profile, name = 'profile'),
    path('like_project/<int:id>/', views.like_project, name = 'like'),
    path('signout/', views.signout, name='signout'),
    path('settings/projects/', views.project_settings, name = 'project-settings'),
    path('delete-project/<int:id>/', views.delete_project, name='delete-project'),
    path('profile/', views.my_profile, name='profile'),
    path('delete-comment/<int:id>/', views.delete_comment, name='delete-comment'),
    path('delete-reply/<int:id>/', views.delete_reply, name='delete-reply'),
    path('settings/', views.settings_general, name = 'settings'),
    path('settings/legal', views.settings_legal, name = 'legal'),
]