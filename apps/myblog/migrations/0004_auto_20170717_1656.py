# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-17 08:56
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_article_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='image',
            new_name='avator',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='background_image',
            field=models.ImageField(default=b'image/default.png', max_length=64, upload_to=b'image/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(default=b'', verbose_name='\u6587\u7ae0\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, verbose_name='\u7c7b\u540d'),
        ),
    ]
