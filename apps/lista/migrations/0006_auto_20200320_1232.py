# Generated by Django 2.0.6 on 2020-03-20 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0005_auto_20200313_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listado',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 3, 20, 12, 32, 16, 730480)),
        ),
    ]
