# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-23 15:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kryptomain', '0015_auto_20180623_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komentarz',
            name='data_wpisu',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 23, 17, 8, 37, 266071), verbose_name='data wpisu'),
        ),
        migrations.AlterField(
            model_name='tematycznypost',
            name='data_wpisu',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 23, 17, 8, 37, 250446), verbose_name='data wpisu'),
        ),
    ]
