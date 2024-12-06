# Generated by Django 5.0.7 on 2024-12-06 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerapp', '0031_alter_ownerprofile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerprofile',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Enter your contact number', max_length=15, null=True),
        ),
    ]