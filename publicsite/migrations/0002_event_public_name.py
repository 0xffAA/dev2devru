# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='public_name',
            field=models.SlugField(default='', max_length=20),
            preserve_default=False,
        ),
    ]