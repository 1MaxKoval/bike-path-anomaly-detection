from django.db import models


class AccelerationLocation(models.Model):
    acceleration = models.DecimalField(max_digits=10, decimal_places=5)
    latitude = models.DecimalField(max_digits=100, decimal_places=10)
    longitude = models.DecimalField(max_digits=100, decimal_places=10)

    class Meta:
        unique_together = ['latitude', 'longitude']


class AccelerationThreshold(models.Model):
    name = models.CharField(max_length=25, unique=True)
    threshold = models.DecimalField(max_digits=10, decimal_places=5)
