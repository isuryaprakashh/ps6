# Generated by Django 5.0.7 on 2024-12-06 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerapp', '0032_alter_ownerprofile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='parking',
            field=models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], default='Available', max_length=20),
        ),
    ]