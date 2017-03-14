# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_auto_20170307_0645'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoiceOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=140)),
            ],
        ),
        migrations.RemoveField(
            model_name='surveyresponse',
            name='customer_age',
        ),
        migrations.AddField(
            model_name='answer',
            name='created_on',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='last_edited_on',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='style',
            field=models.CharField(blank=True, choices=[('rate', 'Rating'), ('text', 'Text Response'), ('mc', 'Multiple Choice')], max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='response_multiple_choice_selected',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.MultipleChoiceOption'),
        ),
        migrations.AddField(
            model_name='question',
            name='choices',
            field=models.ManyToManyField(to='surveys.MultipleChoiceOption'),
        ),
    ]
