# Generated by Django 2.0.6 on 2020-03-05 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'materia',
                'db_table': 'materia',
                'verbose_name_plural': 'materias',
                'ordering': ['-nombre'],
            },
        ),
    ]