# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-23 23:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kryptomain', '0021_auto_20180624_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komentarz',
            name='data_wpisu',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 24, 1, 56, 21, 819106), verbose_name='data wpisu'),
        ),
        migrations.AlterField(
            model_name='tematycznypost',
            name='data_wpisu',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 24, 1, 56, 21, 817107), verbose_name='data wpisu'),
        ),
    ]
