# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='learn_times',
            field=models.IntegerField(default=0, verbose_name='\u89c6\u9891\u65f6\u957f'),
        ),
    ]