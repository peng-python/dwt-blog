# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-28 05:28
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='\u6587\u7ae0\u5185\u5bb9')),
                ('source', models.CharField(default='admin', max_length=50, verbose_name='\u6765\u6e90')),
                ('click_nums', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u91cf')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u53d1\u8868\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='ColumnModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u680f\u76ee')),
                ('isDelete', models.BooleanField(default=False)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u680f\u76ee',
                'verbose_name_plural': '\u680f\u76ee',
            },
        ),
        migrations.CreateModel(
            name='LabelModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u6807\u7b7e')),
                ('isDelete', models.BooleanField(default=False)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_blog.ColumnModel', verbose_name='\u6240\u5c5e\u680f\u76ee'),
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_blog.LabelModel', verbose_name='\u6807\u7b7e'),
        ),
    ]