# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator

class SignInForm(forms.Form):
	userid = forms.CharField()
	password = forms.CharField()

class SignUpForm(forms.Form):
	userid = form.CharField()
	email = form.EmailField()
	password = forms.CharField()