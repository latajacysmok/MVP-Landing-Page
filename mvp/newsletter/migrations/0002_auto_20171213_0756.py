# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-13 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(default='Enter text', max_length=255, null=True),
        ),
    ]
