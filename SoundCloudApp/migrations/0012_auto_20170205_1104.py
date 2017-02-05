# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SoundCloudApp', '0011_auto_20170205_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_lighted',
        ),
        migrations.RemoveField(
            model_name='song',
            name='song_lighted',
        ),
    ]
