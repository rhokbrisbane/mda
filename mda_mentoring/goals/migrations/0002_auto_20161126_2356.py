# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='name',
            field=models.CharField(max_length=200, default='A Goal'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='high_evaluation',
            field=models.CharField(max_length=200, default='A high evaluation'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='low_evaluation',
            field=models.CharField(max_length=200, default='A low evaluation'),
        ),
    ]
