# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 06:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20170526_1057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'MySubscriber', 'verbose_name_plural': 'A lot of Subscribers'},
        ),
    ]
