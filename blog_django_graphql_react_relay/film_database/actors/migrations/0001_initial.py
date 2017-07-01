# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-27 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.PositiveSmallIntegerField()),
                ('rating', models.CharField(choices=[(1, 'did not like him/her'), (2, 'she/he was ok'), (3, 'liked him/her'), (4, 'really liked him/her'), (5, 'she/he was amazing')], max_length=2)),
            ],
        ),
    ]
