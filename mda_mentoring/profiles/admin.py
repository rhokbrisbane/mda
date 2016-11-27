from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import Profile


class ProfileAdmin(UserAdmin):
  fieldsets = UserAdmin.fieldsets + (
    (None, {'fields': ('experience', 'mentee', 'phone_number', 'is_mentor', 'slack_username', 'field', 'qualification', 'language' )}),
  )

admin.site.register(Profile, ProfileAdmin)
