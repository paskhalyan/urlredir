# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-20 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redir', '0005_shorturl_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='url',
            field=models.URLField(),
        ),
    ]