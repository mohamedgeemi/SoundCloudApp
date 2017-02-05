# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SoundCloudApp', '0010_auto_20170205_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_lighted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='song',
            name='song_lighted',
            field=models.BooleanField(default=False),
        ),
    ]
