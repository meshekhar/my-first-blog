# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-25 01:05
from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
    ]
