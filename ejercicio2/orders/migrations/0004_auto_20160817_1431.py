# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-17 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20160817_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minicomponente',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='minicomponente', to='orders.Order', verbose_name='orden'),
        ),
    ]
