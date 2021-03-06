# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-14 08:06
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.TextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe8\xbf\x91\xe7\xbc\x96\xe8\xbe\x91\xe6\x97\xb6\xe9\x97\xb4')),
                ('status', models.CharField(choices=[(b'd', b'Draft'), (b'p', b'Published')], max_length=1, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\x8a\xb6\xe6\x80\x81')),
                ('abstract', models.CharField(blank=True, help_text=b'\xe5\x8f\xaf\xe9\x80\x89\xef\xbc\x8c\xe5\xa6\x82\xe8\x8b\xa5\xe4\xb8\xba\xe7\xa9\xba\xe5\xb0\x86\xe6\x91\x98\xe5\x8f\x96\xe6\xad\xa3\xe6\x96\x87\xe5\x89\x8d54\xe4\xb8\xaa\xe5\xad\x97\xe7\xac\xa6', max_length=54, null=True, verbose_name=b'\xe6\x91\x98\xe8\xa6\x81')),
                ('views', models.PositiveIntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe9\x87\x8f')),
                ('topped', models.BooleanField(default=False, verbose_name=b'\xe7\xbd\xae\xe9\xa1\xb6')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u5206\u7c7b')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe\xe5\x90\x8d')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u70b9\u8d5e\u65f6\u95f4')),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myblog.Article', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myblog.Category', verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='myblog.Tag', verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe\xe9\x9b\x86\xe5\x90\x88'),
        ),
    ]
