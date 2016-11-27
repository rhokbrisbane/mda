# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0004_goal_eval_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(default="Here's an action to complete my milestone", max_length=200)),
                ('milestone', models.ForeignKey(to='goals.Milestone')),
            ],
        ),
    ]
