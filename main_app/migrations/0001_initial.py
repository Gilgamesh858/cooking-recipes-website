# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 17:51
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Commento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IngredienteRicetta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantita', models.CharField(max_length=20)),
                ('id_ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Ingrediente')),
            ],
        ),
        migrations.CreateModel(
            name='Ricetta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('difficolta', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('tempo_preparazione', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(400), django.core.validators.MinValueValidator(1)])),
                ('gradimento', models.IntegerField(default=0)),
                ('preparazione', models.CharField(max_length=500)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Sottocategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='ricetta',
            name='id_sottocategoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Sottocategoria'),
        ),
        migrations.AddField(
            model_name='ingredientericetta',
            name='id_ricetta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Ricetta'),
        ),
        migrations.AddField(
            model_name='commento',
            name='id_ricetta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Ricetta'),
        ),
        migrations.AlterUniqueTogether(
            name='ingredientericetta',
            unique_together=set([('id_ricetta', 'id_ingrediente')]),
        ),
    ]
