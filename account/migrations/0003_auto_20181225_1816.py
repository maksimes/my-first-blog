# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-25 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20181225_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='personprofile',
            name='city',
            field=models.CharField(default='', max_length=30, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='personprofile',
            name='gender',
            field=models.CharField(choices=[('MAN', 'Мужской'), ('WOMAN', 'Женский')], max_length=5, verbose_name='Пол'),
        ),
    ]
