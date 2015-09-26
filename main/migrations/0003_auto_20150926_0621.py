# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alerta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alerta',
            old_name='palavras_chaves',
            new_name='palavras_chave',
        ),
    ]
