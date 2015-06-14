# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=50, verbose_name='\ud328\uc2a4\uc6cc\ub4dc')),
                ('nickname', models.CharField(max_length=50, verbose_name='\ubcc4\uba85')),
                ('hy_mail', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\uc720\uc800\uc815\ubcf4',
                'verbose_name_plural': '\uc720\uc800\uc815\ubcf4',
            },
        ),
    ]
