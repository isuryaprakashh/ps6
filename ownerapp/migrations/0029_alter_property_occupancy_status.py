# Generated by Django 5.0.7 on 2024-12-04 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerapp', '0028_alter_property_location_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='occupancy_status',
            field=models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], default='Available', max_length=20),
        ),
    ]