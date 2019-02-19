# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-19 08:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
