# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 10:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kryptomain', '0036_auto_20180625_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komentarz',
            name='data_wpisu',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 25, 12, 44, 56, 451746), verbose_name='data wpisu'),
        ),
        migrations.AlterField(
            model_name='tematycznypost',
            name='data_wpisu',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 25, 12, 44, 56, 450747), verbose_name='data wpisu'),
        ),
    ]
