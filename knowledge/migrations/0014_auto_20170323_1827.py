# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 10:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0013_auto_20170323_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 3, 23, 10, 27, 56, 914944, tzinfo=utc), verbose_name='上传时间'),
        ),
    ]
