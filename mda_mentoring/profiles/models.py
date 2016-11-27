from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):

    phone_number = models.CharField(max_length=12)
    experience = models.TextField(null=True, blank=True)
    language = models.TextField(null=True, blank=True)
    qualification = models.TextField(null=True, blank=True)
    slack_token = models.TextField(null=True, blank=True)
    profile_type = models.CharField(max_length = 6, null=True, blank=True)
    field = models.TextField(null=True, blank=True)
    mentee = models.ForeignKey('self', null=True, blank=True)
    is_mentor = models.BooleanField(null=False, default=False)
    slack_username = models.CharField(max_length = 100, null=True, blank=True)

    def __unicode__(self):
        return self.username
