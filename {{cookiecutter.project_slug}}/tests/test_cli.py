#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `{{ cookiecutter.project_slug }}` package."""

from click.testing import CliRunner

import {{ cookiecutter.package_name }}
from {{ cookiecutter.package_name }} import cli

{{ cookiecutter.package_name }}.__version__


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.package_name }}.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
