# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-10-26 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0004_projects_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='info',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='info',
            field=models.CharField(max_length=50),
        ),
    ]
