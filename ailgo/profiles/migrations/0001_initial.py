# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-12-14 14:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approx_duration_month', models.IntegerField(default=2)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('days_to_take', models.IntegerField(default=2)),
                ('no_of_time', models.IntegerField(default=2)),
                ('starting_date', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Presciptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('ailment', models.TextField(blank=True, null=True)),
                ('allergies', models.ManyToManyField(blank=True, to='profiles.Allergies')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor')),
                ('medicine', models.ManyToManyField(blank=True, to='profiles.Medicines')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('is_working', models.BooleanField(default=False)),
                ('gender', models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE'), (3, 'NA')], default=1)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Contacts')),
            ],
        ),
        migrations.AddField(
            model_name='presciptions',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.User'),
        ),
        migrations.AddField(
            model_name='allergies',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.User'),
        ),
    ]