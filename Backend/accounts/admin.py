from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from . models import User

from . forms import CustomUserChangeForms, CustomUserCreateForms

class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    add_form = CustomUserCreateForms
    form = CustomUserChangeForms
    model = User
    list_display = ['pkid', 'id', 'email', 'first_name', 'username', 'last_name','is_staff', 'is_active']
    list_display_links = ['id', 'email', 'username']
    list_filter = ['id', 'email', 'first_name', 'username', 'last_name','is_staff', 'is_active']
    
    fieldsets = (
        
    )