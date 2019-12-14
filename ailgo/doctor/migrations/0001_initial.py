# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-12-14 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('experience', models.IntegerField(default=0)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Contacts')),
            ],
        ),
    ]
