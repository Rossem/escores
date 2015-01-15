# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150114_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LoLPosition',
            fields=[
                ('position_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='main.Position')),
                ('position', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=('main.position',),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.ForeignKey(to='main.Position'),
            preserve_default=True,
        ),
    ]
