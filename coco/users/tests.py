# -*- coding: utf-8 -*-
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from users.views import (
    sign_up,
    login
)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_sign_up(self):
        found = resolve('/')
        self.assertEqual(found.func, sign_up)

    def test_sign_up_returns_correct_html(self):
        request = HttpRequest()
        request.user = None
        response = sign_up(request)
        self.assertIn(b'<title>가입하기 | 한양중고장터</title>', response.content)

    def test_login_returns_correct_html(self):
        request = HttpRequest()
        request.user = None
        response = login(request)
        self.assertIn(b'<title>로그인 | 한양중고장터</title>', response.content)
