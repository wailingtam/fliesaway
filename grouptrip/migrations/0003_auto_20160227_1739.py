# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grouptrip', '0002_auto_20160227_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trippreferences',
            name='budget',
            field=models.IntegerField(default=None),
        ),
    ]
