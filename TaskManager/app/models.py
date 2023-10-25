from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractUser):
    
    email = models.EmailField(unique=True)
    # USERNAME_FIELD = 'email'
    
    


class Task(models.Model):
    status = (
        ("Complete","Complete"),
        ("Pending","Pending"),
    )
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    task = models.CharField(max_length=100, null = True , blank = True )
    task_desc = models.CharField(max_length=200, null = True , blank = True )
    status = models.CharField(max_length=10, choices= status,default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)