# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-27 06:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0003_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='qa.Question'),
        ),
    ]
