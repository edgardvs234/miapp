# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-08 19:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_noticias'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noticias',
            options={'managed': False},
        ),
    ]