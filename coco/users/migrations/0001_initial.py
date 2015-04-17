# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usename', models.CharField(help_text=b'id', unique=True, max_length=20, verbose_name=b'id', db_index=True)),
                ('displayname', models.CharField(max_length=20, verbose_name=b'nickname', blank=True)),
                ('email', models.EmailField(max_length=255, unique=True, null=True, verbose_name='Email')),
                ('is_active', models.BooleanField(default=False, help_text=b'Is this user active?', verbose_name=b'is active')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name=b'last_login')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name=b'created_at')),
            ],
            options={
                'swappable': 'AUTH_USER_MODEL',
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
