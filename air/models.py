# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Api(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    temp = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'api'


class Aqi(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    pmlevel = models.FloatField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'aqi'


class Kidbright(models.Model):
    ts = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    lux = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kidbright'


class Projects(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    pm10 = models.FloatField()
    pm2_5 = models.FloatField()
    temp = models.FloatField()
    humidity = models.FloatField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'projects'


class Second(models.Model):
    time = models.CharField(max_length=16, blank=True, null=True)
    temperature_2m_c_field = models.DecimalField(db_column='temperature_2m (°C)', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    wind_speed_10m_km_h_field = models.DecimalField(db_column='wind_speed_10m (km/h)', max_digits=3, decimal_places=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    wind_speed_80m_km_h_field = models.DecimalField(db_column='wind_speed_80m (km/h)', max_digits=3, decimal_places=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    wind_direction_10m_field = models.IntegerField(db_column='wind_direction_10m (°)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    wind_direction_80m_field = models.IntegerField(db_column='wind_direction_80m (°)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    relative_humidity_2m_field = models.IntegerField(db_column='relative_humidity_2m (%)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'second'


class Tmd(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    temp = models.FloatField()
    humidity = models.FloatField()
    rainfall = models.FloatField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tmd'


class Weather(models.Model):
    ts = models.DateTimeField()
    lat = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    lon = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    sensor = models.CharField(max_length=11)
    source = models.CharField(max_length=9)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'weather'
