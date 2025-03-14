# Generated by Django 5.1.6 on 2025-03-11 13:47

import cloudinary.models
import reviews.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_delete_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='excerpt',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, validators=[reviews.models.validate_image_size], verbose_name='image'),
        ),
    ]
