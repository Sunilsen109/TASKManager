from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('', home , name = 'home' ),
    path('task', task , name = 'task' ),
    path('add-task', add_task , name = 'add_task' ),
    path('update-task/<int:id>', update_task , name = 'update_task' ),
    path('delete-task/<int:id>', delete_task , name = 'delete_task' ),
    path('task', task , name = 'task' ),
    path('profile', profile, name = 'profile' ),
    

    path('register/', signup, name='register'),
    path('login/',  LoginView.as_view(), name='login'),
    
    path('logout/',  LogoutView.as_view(), name='logout'),
]
