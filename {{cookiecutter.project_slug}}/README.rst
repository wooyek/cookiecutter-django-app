{% set is_open_source = cookiecutter.open_source_license != 'Propertiary' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

{% if cookiecutter.use_travis_ci == 'y' -%}
.. image:: https://img.shields.io/travis/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}
{%- endif %}

{% if cookiecutter.use_read_the_docs == 'y' -%}
.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}
.. image:: https://coveralls.io/repos/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/badge.svg?branch=develop
        :target: https://coveralls.io/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}?branch=develop
        :alt: Coveralls.io coverage

.. image:: https://codecov.io/gh/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/branch/develop/graph/badge.svg
        :target: https://codecov.io/gh/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}
        :alt: CodeCov coverage

.. image:: https://api.codeclimate.com/v1/badges/0e7992f6259bc7fd1a1a/maintainability
        :target: https://codeclimate.com/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/maintainability
        :alt: Maintainability

.. image:: https://img.shields.io/github/license/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/blob/develop/LICENSE
        :alt: License

.. image:: https://img.shields.io/twitter/url/https/github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}.svg?style=social
        :target: https://twitter.com/intent/tweet?text=Wow:&url={{ cookiecutter.project_url }}
        :alt: Tweet about this project

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
        :target: https://saythanks.io/to/{{ cookiecutter.repo_username }}

{%- endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source -%}
* Free software: {{ cookiecutter.open_source_license }}
{%- else -%}
* Propertiary software of {{ cookiecutter.copyright }}, please obtain a license before use.
{%- endif %}
{% if cookiecutter.use_read_the_docs == 'y' -%}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{%- endif %}

Features
--------

* Pending :D

Demo
----

To run an example project for this django reusable app, click the button below and start a demo serwer on Heroku

.. image:: https://www.herokucdn.com/deploy/button.png
    :target: https://heroku.com/deploy
    :alt: Deploy Django Opt-out example project to Heroku


Quickstart
----------

Install {{ cookiecutter.project_name }}::

    pip install {{ cookiecutter.project_slug }}

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        '{{ cookiecutter.package_name }}.apps.{{ cookiecutter.app_config_name }}',
        ...
    )

Add {{ cookiecutter.project_name }}'s URL patterns:

.. code-block:: python

    from {{ cookiecutter.package_name }} import urls as {{ cookiecutter.package_name }}_urls


    urlpatterns = [
        ...
        url(r'^', include({{ cookiecutter.package_name }}_urls)),
        ...
    ]


Running Tests
-------------

Does the code actually work?

::
    $ pipenv install --dev
    $ pipenv shell
    $ tox


We recommend using pipenv_ but a legacy approach to creating virtualenv and installing requirements should also work.
Please install `requirements/development.txt` to setup virtual env for testing and development.


Credits
-------

This package was created with Cookiecutter_ and the `wooyek/cookiecutter-django-app`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`wooyek/cookiecutter-django-app`: https://github.com/wooyek/cookiecutter-django-app
.. _`pipenv`: https://docs.pipenv.org/install#fancy-installation-of-pipenv
