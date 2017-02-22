# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 05:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0004_auto_20170222_0511'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyapfytmanager',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company'),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]