# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 11:17
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20170720_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
