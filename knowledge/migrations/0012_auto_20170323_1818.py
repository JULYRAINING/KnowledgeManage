# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 10:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0011_auto_20170322_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='knowledge.Category', verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='document',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 3, 23, 10, 18, 22, 51719, tzinfo=utc), verbose_name='上传时间'),
        ),
    ]
