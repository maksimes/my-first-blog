# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-13 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20190109_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='static/avatars/', verbose_name='Фотография'),
        ),
    ]
