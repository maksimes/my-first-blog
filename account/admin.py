from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'gender', 'dateOfBirth', 'avatar']

admin.site.register(Profile, ProfileAdmin)