from django.contrib import admin
from django.urls import path
from .views import *
from knox import views as knox_views

urlpatterns = [
    
    path('', home , name = 'home' ),
    path('task', task , name = 'task' ),
    path('add-task', add_task , name = 'add_task' ),
    path('update-task/<int:id>', update_task , name = 'update_task' ),
    path('delete-task/<int:id>', delete_task , name = 'delete_task' ),
    path('task', task , name = 'task' ),
    path('profile', profile, name = 'profile' ),
    

    # path('register/', register_user.as_view(), name='register'),
    path('register/', signup, name='register'),
    # path('register/', RegistrationAPI.as_view(), name='register'),
    # path('login/', user_login.as_view(), name='login'),
    path('login/',  LoginView.as_view(), name='login'),
    # path('login/',  login_view, name='login'),
    
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('logout-all/', CustomLogoutView.as_view(), name='logout_all'),
]
