# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150114_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='league_abr',
            field=models.CharField(max_length=10, verbose_name=b'League Abbreviation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='league',
            name='league_name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='league',
            name='region',
            field=models.ForeignKey(related_name='leagues', to='main.Region'),
            preserve_default=True,
        ),
    ]
