# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 21:03
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20170717_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
