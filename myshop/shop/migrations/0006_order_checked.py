# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-18 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20180312_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='checked',
            field=models.BooleanField(default=True),
        ),
    ]
