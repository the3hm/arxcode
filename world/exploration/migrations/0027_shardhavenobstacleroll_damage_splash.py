# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-15 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exploration', '0026_auto_20181115_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='shardhavenobstacleroll',
            name='damage_splash',
            field=models.BooleanField(default=False, verbose_name='Should damage hit others in the party too?'),
        ),
    ]
