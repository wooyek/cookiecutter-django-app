import os
from contextlib import contextmanager

import pytest
import sh
from cookiecutter.utils import rmtree

QUICK_CONTEXT = {
    'git_init': 'n',
    'run_tests_on_init': 'n',
    'create_virtual_environment': 'n',
}

@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies, cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        # assert result.error is None
        assert result.exception is None, getattr(result.exception, 'error', result.exception)
        yield result
    finally:
        rmtree(str(result.project))


def test_bake_selecting_license(cookies):
    """
    Test to check if the LICENSE gets the correct license selected
    """

    license_strings = {
        'Apache Software License 2.0': 'Apache',
        'BSD license': 'Redistributions of source code must retain the above copyright notice, this',
        'ISC license': 'Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee',
        'MIT license': 'MIT ',
    }
    for license, target_string in license_strings.items():
        extra_context = dict(QUICK_CONTEXT, open_source_license=license)
        with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
            assert target_string in result.project.join('LICENSE').read()
            assert license in result.project.join('setup.py').read()


def test_readme(cookies):
    extra_context = dict(QUICK_CONTEXT, package_name='helloworld')
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        readme_file = result.project.join('README.rst')
        readme_lines = [x.strip() for x in readme_file.readlines(cr=False)]
        assert 'Add it to your `INSTALLED_APPS`:' in readme_lines
        assert '$ pipenv install --dev' in readme_lines


def test_urls_without_model(cookies):
    """
    Test case to assert that the urls.py file has the basic template when there are no models defined
    """
    extra_context = dict(QUICK_CONTEXT, package_name='cookies')
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        urls_file = result.project.join('src', 'cookies', 'urls.py')
        urls_file_txt = urls_file.read()
        basic_url = "url(r'', TemplateView.as_view(template_name=\"cookies/base.html\"))"
        assert basic_url in urls_file_txt


def test_templates(cookies):
    pass


def test_travis(cookies):
    extra_context = dict(QUICK_CONTEXT, package_name='cookie_lover')
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        travis_file = result.project.join('.travis.yml')
        travis_text = travis_file.read()
        assert 'script:\n  - tox --skip-missing-interpreters' in travis_text


def test_tox(cookies):
    extra_context = dict(QUICK_CONTEXT, package_name='cookie_lover')
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        tox_file = result.project.join('tox.ini')
        tox_text = tox_file.read()
        # assert 'commands = coverage run --source cookie_lover runtests.py' in tox_text
        cmd = """commands =
    coverage run  --source src --parallel-mode setup.py test"""
        assert cmd in tox_text


def test_authors(cookies):
    extra_context = dict(QUICK_CONTEXT, full_name='Cookie McCookieface')
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        authors_file = result.project.join('AUTHORS.rst')
        authors_text = authors_file.read()
        assert 'Cookie McCookieface' in authors_text

def test_setup_py(cookies):
    extra_context = dict(QUICK_CONTEXT, package_name='cookie_lover', full_name='Cookie McCookieface')
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        setup_file = result.project.join('setup.py')
        setup_text = setup_file.read()
        assert "version=version" in setup_text
        assert '    author="Cookie McCookieface",' in setup_text


def test_flake8_compliance(cookies):
    """generated project should pass flake8"""
    extra_context = dict(QUICK_CONTEXT, create_example_project='Y')
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        for file_obj in result.project.listdir():
            name = os.path.join(
                file_obj.dirname,
                file_obj.basename
            )
            if not name.endswith('.py'):
                continue
            try:
                sh.flake8(name)
            except sh.ErrorReturnCode as e:
                pytest.fail(str(e))


def test_app_config(cookies):
    extra_context = dict(QUICK_CONTEXT, package_name='cookie_lover')
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        apps_file = result.project.join('src', 'cookie_lover', 'apps.py')
        apps_text = apps_file.read()
        assert 'CookieLoverConfig' in apps_text
        assert "name = 'cookie_lover'" in apps_text
        readme_file = result.project.join('README.rst')
        readme_text = readme_file.read()
        assert "'cookie_lover.apps.CookieLoverConfig'," in readme_text


@pytest.mark.skip(reason="src/package_name is not on path")
def test_make_migrations(cookies):
    """generated project should be able to generate migrations"""
    extra_context = dict(QUICK_CONTEXT.copy())#, create_virtual_environment='y')
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        res = result.project.join('manage.py')
        src = result.project.join('src')
        try:
            sh.python(res, 'makemigrations', _env={"PYTHONPATH": src})
        except sh.ErrorReturnCode as e:
            pytest.fail(str(e))


@pytest.mark.skip(reason="src/package_name is not on path")
def test_run_tests(cookies):
    """generated project should run tests"""
    extra_context = dict(QUICK_CONTEXT, package_name='cookie_lover')
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        res = result.project.join('runtests.py')
        try:
            sh.python(res)
        except sh.ErrorReturnCode as e:
            pytest.fail(str(e))
