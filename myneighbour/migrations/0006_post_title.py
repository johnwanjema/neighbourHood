# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-12 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myneighbour', '0005_remove_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='tiger', max_length=150),
            preserve_default=False,
        ),
    ]