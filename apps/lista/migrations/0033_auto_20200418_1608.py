# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-18 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0032_listado_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listado',
            name='estado',
            field=models.IntegerField(blank=True, choices=[(0, 'Matriculado'), (1, 'Retirado'), (2, 'Suspendido'), (3, 'Finalizado')], default=0, null=True),
        ),
    ]