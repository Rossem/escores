# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('league_name', models.CharField(max_length=30)),
                ('league_abr', models.CharField(max_length=10)),
                ('num_of_teams', models.IntegerField(default=0)),
                ('region', models.CharField(max_length=20)),
                ('game', models.ForeignKey(related_name='leagues', to='main.Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('league', models.ForeignKey(to='main.League')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16)),
                ('full_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=10)),
                ('free_agent', models.BooleanField(default=True)),
                ('game', models.ForeignKey(to='main.Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('draws', models.IntegerField(default=0)),
                ('league', models.ForeignKey(to='main.League')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=20)),
                ('team_name_abr', models.CharField(max_length=4)),
                ('game', models.ForeignKey(related_name='teams', to='main.Game')),
                ('league', models.ForeignKey(related_name='teams', to='main.League')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='stats',
            name='team',
            field=models.ForeignKey(related_name='stats', to='main.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='main.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='region',
            field=models.ForeignKey(related_name='news_stories', to='main.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(related_name='team1', to='main.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='team2',
            field=models.ForeignKey(related_name='team2', to='main.Team'),
            preserve_default=True,
        ),
    ]
