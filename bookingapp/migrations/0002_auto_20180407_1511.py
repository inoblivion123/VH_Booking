# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-04-07 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='last_name',
        ),
        migrations.AddField(
            model_name='post',
            name='check_in',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='check_out',
            field=models.DateField(null=True),
        ),
    ]
