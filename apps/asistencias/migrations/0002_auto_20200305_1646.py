# Generated by Django 2.0.6 on 2020-03-05 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('horario', '0001_initial'),
        ('lista', '0001_initial'),
        ('asistencias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencias',
            name='Horario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='horario.Horario'),
        ),
        migrations.AddField(
            model_name='asistencias',
            name='Listado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lista.Listado'),
        ),
    ]