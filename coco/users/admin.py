# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from users.models import BaseUser

class BaseUserInline(admin.StackedInline):
	model = BaseUser
	can_delete = False
	verbose_name_plural = '유저정보'

class UserAdmin(UserAdmin):
	inlines = (BaseUserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)