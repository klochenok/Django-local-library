# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance', options={
                'ordering': ['due_back'], 'permissions': (
                    ('can_mark_returned', 'Set book as returned'),)}, ), ]