# Generated by Django 5.0.7 on 2024-12-06 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerapp', '0034_alter_property_parking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='parking',
            field=models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], default='Available', max_length=20),
        ),
    ]
