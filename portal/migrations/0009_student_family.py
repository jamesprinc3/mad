# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-09 20:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_family'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='family',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Family'),
        ),
    ]