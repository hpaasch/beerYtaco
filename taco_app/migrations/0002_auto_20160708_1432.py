# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taco_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drink',
            old_name='notes',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='extra',
            old_name='notes',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='notes',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='drink',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='extra',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='food',
            name='quantity',
        ),
        migrations.AddField(
            model_name='customerorder',
            name='notes',
            field=models.CharField(default=2, max_length=250),
            preserve_default=False,
        ),
    ]