# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 18:24
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_dealoftheday_removed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealoftheday',
            name='image',
            field=image_cropping.fields.ImageCropField(upload_to='images/dotd/'),
        ),
    ]