# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 10:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20170606_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinorder',
            name='order',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
    ]