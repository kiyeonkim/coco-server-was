from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group
from django import forms
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, username, password, displayname, email , **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.displayname = displayname
        user.email = email
        user.is_active = True
        user.date_joined = timezone.now()
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        swappable = "AUTH_USER_MODEL"

    username = models.CharField(verbose_name="username",
                              max_length=30,
                              unique=True,
                              null=False)

    displayname = models.CharField(verbose_name="nickname",
        max_length=20,
        null=False,
        blank=True)

    email = models.EmailField(verbose_name="Email",
        max_length=255,
        unique=True,
        null=True)

    is_active = models.BooleanField(verbose_name="is active",
                                    default=True,
                                    help_text="Is this user active?")

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'

    objects = UserManager()
