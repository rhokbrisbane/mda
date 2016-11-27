# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0003_milestone_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='eval_date',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
