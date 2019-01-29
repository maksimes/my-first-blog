# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-08 21:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20190103_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='static/avatars/', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dateOfBirth',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата рождения'),
        ),
    ]