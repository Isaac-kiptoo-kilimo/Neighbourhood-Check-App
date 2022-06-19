# Generated by Django 4.0.5 on 2022-06-19 07:19

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_neighbourhood_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='business_logo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='business',
            name='contact',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]