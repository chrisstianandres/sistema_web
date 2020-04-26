# Generated by Django 2.0.6 on 2020-03-05 21:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('docente', '0001_initial'),
        ('alumno', '0001_initial'),
        ('curso', '0001_initial'),
        ('silabo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('observacion', models.CharField(max_length=200)),
                ('alumno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alumno.Alumno')),
            ],
            options={
                'verbose_name': 'actividad',
                'db_table': 'actividad',
                'verbose_name_plural': 'actividades',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciclo', models.IntegerField(choices=[(1, 'Primero'), (2, 'Segundo')], default=1)),
                ('hora_inicio', models.CharField(max_length=5)),
                ('hora_fin', models.CharField(max_length=5)),
                ('fecha', models.DateField(default=datetime.datetime.now)),
                ('estado', models.IntegerField(choices=[(1, 'Falta'), (2, 'Registrado')], default=1)),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='curso.Curso')),
                ('docente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='docente.Docente')),
                ('silabo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='silabo.Silabo')),
            ],
            options={
                'verbose_name': 'horario',
                'db_table': 'horario',
                'verbose_name_plural': 'horarios',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='actividad',
            name='horario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='horario.Horario'),
        ),
    ]