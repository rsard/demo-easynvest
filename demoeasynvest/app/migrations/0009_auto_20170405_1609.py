# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20170404_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo',
            name='ano',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='mes',
            field=models.CharField(max_length=255),
        ),
    ]