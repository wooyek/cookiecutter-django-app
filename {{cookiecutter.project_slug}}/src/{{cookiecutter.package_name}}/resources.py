# coding=utf-8
from import_export import resources, widgets

from . import models


class SampleModelResource(resources.ModelResource):
    class Meta:
        model = models.SampleModel
