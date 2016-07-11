# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 01:42
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
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tag_number', models.SlugField(null=True)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='add drink', max_length=20)),
                ('description', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=20, null=True)),
                ('role', models.CharField(choices=[('Server', 'Server'), ('Bartender', 'Bartender'), ('Cook', 'Cook'), ('Manager', 'Manager')], default='Server', max_length=20)),
                ('preferred_language', models.CharField(choices=[('English', 'English'), ('Spanish', 'Spanish')], default='English', max_length=20)),
                ('worker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='add extra', max_length=20)),
                ('description', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='add taco', max_length=20)),
                ('tortilla', models.CharField(max_length=20)),
                ('protein', models.CharField(max_length=20)),
                ('dress', models.CharField(max_length=60)),
                ('finish', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDrink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=250, null=True)),
                ('order_up', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('drink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taco_app.Drink')),
                ('order_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taco_app.Customer')),
                ('placed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', 'order_tag'],
            },
        ),
        migrations.CreateModel(
            name='OrderFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_quantity', models.PositiveIntegerField(default=0, null=True)),
                ('extra_quantity', models.PositiveIntegerField(default=0, null=True)),
                ('notes', models.CharField(blank=True, max_length=250, null=True)),
                ('order_up', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('extra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taco_app.Extra')),
                ('food', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taco_app.Food')),
                ('order_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taco_app.Customer')),
                ('placed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
