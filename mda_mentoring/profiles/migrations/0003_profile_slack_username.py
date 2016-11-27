# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_is_mentor'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slack_username',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
