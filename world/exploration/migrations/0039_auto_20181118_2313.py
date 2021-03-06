# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-18 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exploration', '0038_shardhaven_auto_combat'),
    ]

    operations = [
        migrations.AddField(
            model_name='shardhavenobstacle',
            name='modified_diff_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shardhavenobstacle',
            name='modified_diff_by',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shardhavenobstacle',
            name='modified_diff_reason',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
