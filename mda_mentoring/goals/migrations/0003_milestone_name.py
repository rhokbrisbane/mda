# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_auto_20161126_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='milestone',
            name='name',
            field=models.CharField(default='Give me a name', max_length=200),
        ),
    ]
