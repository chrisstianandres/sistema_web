# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-02 19:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0010_auto_20200327_1948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notas',
            options={'verbose_name': 'notas', 'verbose_name_plural': 'notas'},
        ),
        migrations.AlterModelTable(
            name='notas',
            table='notas',
        ),
    ]
