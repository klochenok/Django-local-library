# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 12:22
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('language',
                 models.CharField(
                     blank=True,
                     choices=[
                         ('en',
                          'English'),
                         ('ua',
                          'Ukrainian'),
                         ('ru',
                          'Russian')],
                     default='ua',
                     help_text='Book language',
                     max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='catalog.Language'),
        ),
    ]
