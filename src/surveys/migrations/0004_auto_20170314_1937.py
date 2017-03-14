# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 19:37
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0003_auto_20170314_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='response_rate',
            field=models.PositiveIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=models.ManyToManyField(blank=True, to='surveys.MultipleChoiceOption'),
        ),
    ]
