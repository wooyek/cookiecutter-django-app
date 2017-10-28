# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views as v

app_name = '{{cookiecutter.package_name}}'

urlpatterns = [
    url(r'', TemplateView.as_view(template_name="{{cookiecutter.package_name}}/base.html")),
    url(r'', v.SampleView.as_view()),
]
