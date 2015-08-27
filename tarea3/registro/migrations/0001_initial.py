# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('nom_comuna', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('nom_localidad', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Farmacia',
            fields=[
                ('local', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('local_direccion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'farmacia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('mes', models.IntegerField()),
                ('dia', models.IntegerField()),
            ],
            options={
                'db_table': 'fecha',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('horario', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('hora_ini', models.CharField(max_length=50)),
                ('hora_fin', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'horarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('cod_region', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('nom_region', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
    ]
