# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-23 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
