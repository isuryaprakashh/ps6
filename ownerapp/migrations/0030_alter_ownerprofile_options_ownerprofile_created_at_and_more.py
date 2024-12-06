# Generated by Django 5.0.7 on 2024-12-06 16:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerapp', '0029_alter_property_occupancy_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ownerprofile',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='ownerprofile',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ownerprofile',
            name='email',
            field=models.EmailField(blank=True, help_text='Your email address', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ownerprofile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ownerprofile',
            name='address',
            field=models.TextField(blank=True, help_text='Your complete address', null=True),
        ),
        migrations.AlterField(
            model_name='ownerprofile',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Enter your contact number', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ownerprofile',
            name='profile_image',
            field=models.ImageField(blank=True, help_text='Upload a profile picture (Optional)', null=True, upload_to='profile_images/'),
        ),
    ]