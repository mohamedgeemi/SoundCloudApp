# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SoundCloudApp', '0007_song_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='likers',
        ),
        migrations.AddField(
            model_name='album',
            name='likes',
            field=models.ManyToManyField(related_name='album_likes', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.ManyToManyField(related_name='song_likes', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
