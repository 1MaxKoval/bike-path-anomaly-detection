from rest_framework import serializers
from anomalies.models import AccelerationLocation, AccelerationThreshold


class AccelerationLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccelerationLocation
        fields = ['longitude', 'latitude', 'acceleration']
        extra_kwargs = {
            'longitude': {'max_digits': 100, 'decimal_places': 10},
            'latitude': {'max_digits': 100, 'decimal_places': 10},
            'acceleration': {'max_digits': 10, 'decimal_places': 5, 'min_value': 0}
        }


class AccelerationThresholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccelerationThreshold
        fields = ['name', 'threshold']
        extra_kwargs = {
            'name': {'allow_blank': False, 'max_length': 25, 'required': False, 'read_only': False},
            'threshold': {'max_digits': 10, 'min_value': 0, 'decimal_places': 5}
        }
