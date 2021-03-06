# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('source', models.URLField()),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=250)),
                ('display', models.BooleanField()),
                ('imageurl', models.CharField(max_length=50)),
            ],
        ),
    ]
