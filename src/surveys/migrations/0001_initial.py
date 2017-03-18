# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 03:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_text', models.TextField(blank=True, max_length=500, null=True)),
                ('response_rate', models.PositiveIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('created_on', models.DateField(auto_now_add=True)),
                ('last_edited_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MultipleChoiceOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=500)),
                ('style', models.CharField(blank=True, choices=[('rate', 'Rating'), ('text', 'Text Response'), ('mc', 'Multiple Choice')], max_length=25, null=True)),
                ('required', models.BooleanField(default=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('choices', models.ManyToManyField(blank=True, to='surveys.MultipleChoiceOption')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('reward', models.TextField(blank=True, max_length=500, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('start_time', models.DateField(auto_now_add=True)),
                ('last_edited', models.DateField(auto_now=True)),
                ('apfyt_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ApfytUser')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Survey')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='surveys.Survey'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='response_multiple_choice_selected',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.MultipleChoiceOption'),
        ),
        migrations.AddField(
            model_name='answer',
            name='survey_response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.SurveyResponse'),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('survey', 'question')]),
        ),
    ]
