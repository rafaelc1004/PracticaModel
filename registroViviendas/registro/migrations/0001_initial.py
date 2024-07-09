# Generated by Django 5.0.6 on 2024-07-09 03:14

import registro.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('idPersona', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=50, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateField(default=2006, validators=[registro.validators.validarFecha])),
            ],
        ),
    ]