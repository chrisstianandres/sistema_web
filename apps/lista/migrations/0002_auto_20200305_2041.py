# Generated by Django 2.0.6 on 2020-03-06 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('periodo', '0001_initial'),
        ('lista', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listado',
            name='año',
        ),
        migrations.AddField(
            model_name='listado',
            name='periodo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='periodo.Periodo'),
        ),
    ]
