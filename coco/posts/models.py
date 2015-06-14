# -*- coding: utf-8 -*-
from django.db import models
from users.models import BaseUser

class Post(models.Model):
    class Meta:
        verbose_name = u'게시글'

    title = models.CharField(max_length=50, blank=False)
    user_id = models.ForeignKey(BaseUser)
    content = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    hits = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)