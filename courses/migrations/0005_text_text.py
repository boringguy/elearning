# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='text',
            field=models.TextField(default='Description'),
        ),
    ]
