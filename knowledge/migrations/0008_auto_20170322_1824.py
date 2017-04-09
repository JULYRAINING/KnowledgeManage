# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 10:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0007_auto_20170322_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='knowledge.DocumentStatus', verbose_name='审核状态'),
        ),
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='文件'),
        ),
        migrations.AlterField(
            model_name='document',
            name='is_Markdown',
            field=models.BooleanField(default=False, verbose_name='使用Markdown编辑器'),
        ),
    ]