# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talk', '0003_auto_20170806_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
