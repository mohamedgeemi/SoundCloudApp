# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SoundCloudApp', '0004_auto_20170203_0157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='creator',
            new_name='user',
        ),
    ]
