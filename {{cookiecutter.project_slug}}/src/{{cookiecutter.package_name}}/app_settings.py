# coding=utf-8

from django.conf import settings

# This is an example
{{ cookiecutter.package_name.upper() }}_SECRET = settings.SECRET_KEY[::4]
