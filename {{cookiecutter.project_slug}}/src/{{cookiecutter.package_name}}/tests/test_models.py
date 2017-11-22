#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.project_slug }}
------------

Tests for `{{ cookiecutter.project_slug }}` models module.
"""

from django.test import TestCase

from .. import models
from .. import factories


class Test{{ cookiecutter.package_name|title|replace("_", "") }}(TestCase):

    def test_something(self):
        self.assertIsNotNone(models)

    def test_user_factory(self):
        user = factories.UserFactory()
        self.assertIsNotNone(user)
