# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-14 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20170714_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=b'article/default.png', max_length=64, upload_to=b'article/%Y/%m', verbose_name='\u5c01\u9762\u56fe'),
        ),
    ]
