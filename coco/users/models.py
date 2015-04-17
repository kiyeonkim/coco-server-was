from django.db import models
from django import forms

class Users(models.Model):
	class Meta:
		verbose_name = "user"
		verbose_name_plural = "users"
		swappable = "AUTH_USER_MODEL"

	usename = models.CharField(verbose_name="id",
		max_length=20,
		help_text="id",
		unique=True,
		null=False,
		db_index=True)

	password = forms.CharField(widget=forms.PasswordInput())

	displayname = models.CharField(verbose_name="nickname",
		max_length=20,
		null=False,
		blank=True)
	email = models.EmailField(verbose_name=u"Email",
		max_length=255,
		unique=True,
		null=True)

	is_active = models.BooleanField(verbose_name="is active",
		default=False,
		help_text="Is this user active?")

	last_login = models.DateTimeField(verbose_name="last_login",
		auto_now_add=True)
	created_at = models.DateTimeField(verbose_name="created_at",
		auto_now=True)



# Create your models here.
