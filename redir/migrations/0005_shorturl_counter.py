# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-14 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redir', '0004_auto_20181112_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]
