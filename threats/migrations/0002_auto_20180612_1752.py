# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-12 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import rest_framework.views


class Migration(migrations.Migration):

    dependencies = [
        ('threats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traffic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('timestamp', models.TextField()),
                ('endpoint', models.TextField()),
                ('alienvault_id', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Stat',
        ),
        migrations.CreateModel(
            name='APIRoot',
            fields=[
                ('traffic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='threats.Traffic')),
            ],
            bases=('threats.traffic', rest_framework.views.APIView),
        ),
        migrations.CreateModel(
            name='IPDetailsView',
            fields=[
                ('traffic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='threats.Traffic')),
            ],
            bases=('threats.traffic', rest_framework.views.APIView),
        ),
    ]
