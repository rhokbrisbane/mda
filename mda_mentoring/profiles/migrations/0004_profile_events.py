# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_total_attendees'),
        ('profiles', '0003_profile_slack_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='events',
            field=models.ManyToManyField(blank=True, to='events.Event'),
        ),
    ]
