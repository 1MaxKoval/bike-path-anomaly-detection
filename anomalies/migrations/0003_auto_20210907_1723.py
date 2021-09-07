# Generated by Django 3.2.5 on 2021-09-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anomalies', '0002_accelerationthreshold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accelerationlocation',
            name='latitude',
            field=models.DecimalField(decimal_places=10, max_digits=100),
        ),
        migrations.AlterField(
            model_name='accelerationlocation',
            name='longitude',
            field=models.DecimalField(decimal_places=10, max_digits=100),
        ),
    ]
