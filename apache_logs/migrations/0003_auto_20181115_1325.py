# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-15 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apache_logs', '0002_apacheerrorlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apacheerrorlog',
            name='full_line',
            field=models.TextField(unique=True),
        ),
    ]
