# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-06-21 03:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kryptomain', '0009_auto_20180621_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komentarz',
            name='data_wpisu',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 21, 5, 36, 9, 701334), verbose_name='data wpisu'),
        ),
        migrations.AlterField(
            model_name='tematycznypost',
            name='data_wpisu',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 21, 5, 36, 9, 701334), verbose_name='data wpisu'),
        ),
    ]
