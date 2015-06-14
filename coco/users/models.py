# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

class BaseUser(models.Model):
	class Meta:
		verbose_name = u'유저정보'
		verbose_name_plural = u'유저정보'
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	password = models.CharField(verbose_name=u'패스워드', max_length=50, blank=False)
	nickname = models.CharField(verbose_name=u'별명', max_length=50, blank=False)
	hy_mail = models.EmailField(blank=False)
