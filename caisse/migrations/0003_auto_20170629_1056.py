# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-29 10:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caisse', '0002_auto_20170629_1044'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Popote',
            new_name='Stock',
        ),
    ]