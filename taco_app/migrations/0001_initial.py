# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 19:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('portion', models.CharField(max_length=5)),
                ('quantity', models.IntegerField()),
                ('notes', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20)),
                ('preferred_language', models.CharField(max_length=20)),
                ('worker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('notes', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tortilla', models.CharField(max_length=20)),
                ('protein', models.CharField(max_length=20)),
                ('dress', models.CharField(max_length=20)),
                ('finish', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('notes', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.AddField(
            model_name='customerorder',
            name='drink_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taco_app.Drink'),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='extra_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taco_app.Extra'),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='food_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taco_app.Food'),
        ),
    ]