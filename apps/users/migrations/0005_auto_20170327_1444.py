# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_banner_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('MAN', '\u7537'), ('FEMALE', '\u5973')], default='MAN', max_length=6, verbose_name='\u6027\u522b'),
        ),
    ]
