from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    exclude=("user",)
    readonly_fields=('user', )