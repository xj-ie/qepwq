# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-10-09 08:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategroyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='类别名')),
                ('categroy', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='indexs.CategroyModel', verbose_name='类别上级')),
            ],
            options={
                'db_table': 'categroyMovieTable',
            },
        ),
    ]
