# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-28 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(default='Title', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='desc',
            field=models.TextField(default='Enter Description here...'),
        ),
    ]
