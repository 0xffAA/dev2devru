# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-07 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicsite', '0011_auto_20160906_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('map_center_latitude', models.FloatField(null=True)),
                ('map_center_longitude', models.FloatField(null=True)),
                ('map_zoom', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['date']},
        ),
        migrations.RemoveField(
            model_name='eventpublication',
            name='map_center_latitude',
        ),
        migrations.RemoveField(
            model_name='eventpublication',
            name='map_center_longitude',
        ),
        migrations.RemoveField(
            model_name='eventpublication',
            name='map_zoom',
        ),
        migrations.RemoveField(
            model_name='point',
            name='event',
        ),
        migrations.AlterField(
            model_name='point',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='points', to='publicsite.Section'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='map_settings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='publicsite.MapSetting'),
        ),
    ]