# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talk', '0006_pro_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='pro',
            name='art',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pro',
            name='isexp',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]