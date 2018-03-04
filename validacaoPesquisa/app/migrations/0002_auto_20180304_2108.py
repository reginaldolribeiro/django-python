# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carro',
            old_name='marcar',
            new_name='marca',
        ),
        migrations.AlterField(
            model_name='carro',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 4, 21, 8, 20, 403670)),
            preserve_default=True,
        ),
    ]
