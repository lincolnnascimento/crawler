# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150926_0621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='alerta',
            name='palavras_chave',
        ),
        migrations.AddField(
            model_name='alerta',
            name='palavras_chave',
            field=models.ManyToManyField(to='main.Keyword'),
        ),
    ]
