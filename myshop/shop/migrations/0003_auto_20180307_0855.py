# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-07 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180306_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True),
        ),
    ]
