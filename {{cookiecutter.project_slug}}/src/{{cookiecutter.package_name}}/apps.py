# -*- coding: utf-8
from __future__ import absolute_import

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


def setup_app_settings():
    from . import app_settings as defaults
    from django.conf import settings
    for name in dir(defaults):
        if name.isupper() and not hasattr(settings, name):
            setattr(settings, name, getattr(defaults, name))


class {{ cookiecutter.app_config_name }}(AppConfig):
    name = '{{ cookiecutter.package_name }}'
    verbose_name = _('{{ cookiecutter.project_name }}')

    def ready(self):
        setup_app_settings()
