# Generated by Django 2.0.6 on 2020-03-23 22:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0014_auto_20200323_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listado',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 3, 23, 22, 47, 11, 941072)),
        ),
    ]
