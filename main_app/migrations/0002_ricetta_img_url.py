# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ricetta',
            name='img_url',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
