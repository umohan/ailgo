# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-12-14 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('mobile', models.IntegerField()),
                ('alt_mobile', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('email2', models.EmailField(blank=True, max_length=254, null=True)),
                ('permanent_address', models.TextField(blank=True, null=True)),
                ('user_type', models.IntegerField(choices=[(1, 'user'), (2, 'doctor'), (3, 'pathology')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.City')),
            ],
        ),
        migrations.AddField(
            model_name='contacts',
            name='current_locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Locality'),
        ),
    ]
