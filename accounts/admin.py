from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import ProfileModel

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','bloodgroup','city','mobile','avilable']


admin.site.register(ProfileModel,ProfileAdmin)