from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import *

class CustomUserAdmin(UserAdmin):
    # Add or customize fields to display in the admin panel
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Task)
