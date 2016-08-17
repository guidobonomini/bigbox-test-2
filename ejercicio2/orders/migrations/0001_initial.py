# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-17 12:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('INTENDED', 'Preorden'), ('IN_PROGRESS', 'En Progreso'), ('CANCELLED', 'Cancelada'), ('SUCCESSFUL', 'Exitosa')], default='INTENDED', max_length=11, verbose_name='estado')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Female', 'Mujer'), ('Male', 'Hombre')], max_length=6, verbose_name='sexo')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.UserProfile', verbose_name='usuario'),
        ),
    ]