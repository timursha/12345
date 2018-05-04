# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-01 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170621_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Категория товаров', 'verbose_name_plural': 'Категория товаров'},
        ),
        migrations.AddField(
            model_name='product',
            name='price_with_discount',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=10),
        ),
    ]
