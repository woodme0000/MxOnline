# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20170329_2124'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='org',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='\u6240\u5c5e\u673a\u6784'),
        ),
    ]
