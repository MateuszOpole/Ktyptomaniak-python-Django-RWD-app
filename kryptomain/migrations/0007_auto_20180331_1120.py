# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-31 09:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kryptomain', '0006_auto_20180326_0652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='przelew',
            old_name='wartość_kryptowaluty',
            new_name='zaplacono',
        ),
        migrations.RemoveField(
            model_name='waluta',
            name='Wartość_walut_PLN',
        ),
    ]
