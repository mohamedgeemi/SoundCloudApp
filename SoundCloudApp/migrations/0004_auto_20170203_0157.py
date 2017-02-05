# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SoundCloudApp', '0003_album_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='user',
            new_name='creator',
        ),
    ]
