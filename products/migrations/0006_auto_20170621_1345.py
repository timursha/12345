# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20170614_1007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Категория товара', 'verbose_name_plural': 'Категория товаров'},
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, default=None, max_length=50, null=True),
        ),
    ]