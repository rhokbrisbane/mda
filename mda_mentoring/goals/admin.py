from django.contrib import admin
from .models import Goal, Milestone, Action

# Register your models here.

admin.site.register(Goal)
admin.site.register(Milestone)
admin.site.register(Action)
