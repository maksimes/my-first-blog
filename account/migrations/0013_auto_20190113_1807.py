# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-13 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20190113_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d', verbose_name='Фотография'),
        ),
    ]
