# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20170330_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='ingredientrecipe',
            name='amount',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='ingredientrecipe',
            name='id_ingredient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Ingredient'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='ingredientrecipe',
            name='name',
        ),
        migrations.AlterUniqueTogether(
            name='ingredientrecipe',
            unique_together=set([('id_recipe', 'id_ingredient')]),
        ),
    ]