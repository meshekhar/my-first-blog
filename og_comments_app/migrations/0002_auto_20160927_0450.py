# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-27 04:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('og_comments_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentwithuser',
            name='commenter',
        ),
        migrations.RemoveField(
            model_name='commentwithuser',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='commentwithuser',
            name='site',
        ),
        migrations.RemoveField(
            model_name='commentwithuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='CommentWithUser',
        ),
    ]