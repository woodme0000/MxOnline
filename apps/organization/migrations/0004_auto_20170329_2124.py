# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 21:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20170329_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseorg',
            old_name='course_count',
            new_name='course_nums',
        ),
    ]
