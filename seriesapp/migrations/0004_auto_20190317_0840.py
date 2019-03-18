# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-17 08:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seriesapp', '0003_episodes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episodes',
            name='episodesImages',
        ),
        migrations.RemoveField(
            model_name='episodes',
            name='episodesVideo',
        ),
        migrations.RemoveField(
            model_name='episodes',
            name='series',
        ),
        migrations.RemoveField(
            model_name='series',
            name='seriesVideo',
        ),
        migrations.AddField(
            model_name='episodes',
            name='description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes1',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes10',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes11',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes12',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes13',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes14',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes15',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes16',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes17',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes18',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes19',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes2',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes20',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes21',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes22',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes23',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes24',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes3',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes4',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes5',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes6',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes7',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes8',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodes9',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo1',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo10',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo11',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo12',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo13',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo14',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo15',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo16',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo17',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo18',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo19',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo2',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo20',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo21',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo22',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo23',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo24',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo3',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo4',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo5',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo6',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo7',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo8',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='episodesVideo9',
            field=models.FileField(null=True, upload_to=b'Series/EpisodesVideo/'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='genres',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seriesapp.Genre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='episodes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seriesapp.Episodes'),
            preserve_default=False,
        ),
    ]
