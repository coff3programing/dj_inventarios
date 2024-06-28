# Generated by Django 5.0.6 on 2024-06-27 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LaboratoriosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_laboratorio', models.CharField(max_length=255, unique=True, verbose_name='Nombre del laboratorio')),
            ],
            options={
                'verbose_name': 'Laboratorio',
                'verbose_name_plural': 'Laboratorios',
                'db_table': 'Laboratorios',
            },
        ),
        migrations.CreateModel(
            name='MarcasModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_marca', models.CharField(max_length=55, unique=True, verbose_name='Nombre de la marca')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'db_table': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='TipoActivosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo', models.CharField(max_length=55, unique=True, verbose_name='Nombre del equipo')),
            ],
            options={
                'verbose_name': 'Tipo de Activo',
                'verbose_name_plural': 'Tipos de Activos',
                'db_table': 'TipoActivos',
            },
        ),
        migrations.CreateModel(
            name='ActivosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_activo', models.CharField(max_length=12, unique=True, verbose_name='Código del activo')),
                ('estado', models.CharField(choices=[('OPERATIVO', 'OPERATIVO'), ('Mantenimiento', 'Mantenimiento'), ('BUEN ESTADO', 'BUEN ESTADO')], default='OPERATIVO', max_length=15)),
                ('estado_uso', models.CharField(choices=[('NUEVO', 'Nuevo'), ('VIEJO', 'Viejo')], default='NUEVO', max_length=6)),
                ('observacion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='activos/')),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.laboratoriosmodel')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.marcasmodel')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.tipoactivosmodel')),
            ],
            options={
                'verbose_name': 'Activo',
                'verbose_name_plural': 'Activos',
                'db_table': 'Activos',
            },
        ),
    ]