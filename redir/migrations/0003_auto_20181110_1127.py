# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-10 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redir', '0002_shorturl_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorturl',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='shorturl',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='shorturl',
            name='short_url',
            field=models.CharField(default='hello', max_length=15, unique=True),
            preserve_default=False,
        ),
    ]