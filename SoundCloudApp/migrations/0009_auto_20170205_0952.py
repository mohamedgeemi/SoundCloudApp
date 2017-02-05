# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SoundCloudApp', '0008_auto_20170204_2252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='likes',
            new_name='album_likes',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='likes',
            new_name='song_likes',
        ),
    ]
