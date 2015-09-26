# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alerta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=150)),
                ('texto', models.TextField()),
                ('palavras_chaves', models.TextField()),
                ('data_encontro', models.DateField(auto_now_add=True)),
                ('site', models.ForeignKey(to='main.Site')),
            ],
        ),
    ]
