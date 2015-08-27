# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Comuna(models.Model):
    nom_comuna = models.CharField(primary_key=True, max_length=50)
    nom_localidad = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'comuna'


class Farmacia(models.Model):
    local = models.CharField(primary_key=True, max_length=50)
    local_direccion = models.CharField(max_length=50)
    horario = models.ForeignKey('Horarios', db_column='horario')
    cod_region = models.ForeignKey('Region', db_column='cod_region')
    nom_comuna = models.ForeignKey(Comuna, db_column='nom_comuna')

    class Meta:
        managed = False
        db_table = 'farmacia'


class Fecha(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    local = models.ForeignKey(Farmacia, db_column='local')
    mes = models.IntegerField()
    dia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fecha'


class Horarios(models.Model):
    horario = models.CharField(primary_key=True, max_length=50)
    hora_ini = models.CharField(max_length=50)
    hora_fin = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'horarios'


class Region(models.Model):
    cod_region = models.CharField(primary_key=True, max_length=5)
    nom_region = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'region'
