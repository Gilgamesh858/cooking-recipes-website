# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 00:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20170331_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='id_recipe',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
