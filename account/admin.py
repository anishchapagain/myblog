from django.contrib import admin

# Register your models here.

from .models import UserProfile

# class UserProfileAdmin(admin.ModelAdmin):


admin.site.register(UserProfile)