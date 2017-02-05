# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SoundCloudApp', '0009_auto_20170205_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='is_favorite',
        ),
        migrations.RemoveField(
            model_name='song',
            name='is_favorite',
        ),
    ]
