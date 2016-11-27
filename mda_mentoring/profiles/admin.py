from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import Profile


class ProfileAdmin(UserAdmin):

    pass

admin.site.register(Profile, ProfileAdmin)
