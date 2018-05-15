# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-06 03:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('last_buy_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=200)),
                ('last_supply_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier', to='shop.Supplier'),
        ),
    ]
