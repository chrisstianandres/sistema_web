# Generated by Django 2.0.6 on 2020-03-23 22:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0013_auto_20200323_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listado',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 3, 23, 22, 38, 0, 158003)),
        ),
    ]
