# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicsite', '0005_visitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='company',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='position',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
