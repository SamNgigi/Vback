# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_auto_20180226_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.TextField(blank=True),
        ),
    ]
