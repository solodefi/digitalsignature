# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalsignature', '0002_auto_20171027_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='page_height',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='page_width',
            field=models.FloatField(default=0),
        ),
    ]