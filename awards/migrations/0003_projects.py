# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-09 02:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0002_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=50)),
                ('project_photo', models.ImageField(upload_to='projectpics/')),
                ('description', models.TextField(blank=True, max_length=600)),
                ('github_repo', models.CharField(blank=True, max_length=200)),
                ('url', models.CharField(blank=True, max_length=50)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
