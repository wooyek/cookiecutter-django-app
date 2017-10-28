# -*- coding: utf-8 -*-
from django_powerbank.views.auth import StaffRequiredMixin
from django_powerbank.views.mixins import ReturnUrlMx
from pascal_templates.views import CreateView

from . import models


class SampleView(ReturnUrlMx, StaffRequiredMixin, CreateView):
    model = models.SampleModel
