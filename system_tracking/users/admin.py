# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser  # Correct the import to CustomUser

class UserAdmin(BaseUserAdmin):
    model = CustomUser
    # Define fieldsets, add forms, etc.

admin.site.register(CustomUser, UserAdmin)


