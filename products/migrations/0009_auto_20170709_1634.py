# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-09 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_forrepairs'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForRepairsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=True, max_length=128, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Категория ремонта',
                'verbose_name_plural': 'Категория ремонтов',
            },
        ),
        migrations.AlterField(
            model_name='forrepairs',
            name='category',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ForRepairsCategory'),
        ),
    ]
