# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-24 01:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kryptomain', '0026_auto_20180624_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komentarz',
            name='data_wpisu',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 24, 3, 28, 52, 223720), verbose_name='data wpisu'),
        ),
        migrations.AlterField(
            model_name='tematycznypost',
            name='data_wpisu',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 24, 3, 28, 52, 221721), verbose_name='data wpisu'),
        ),
    ]