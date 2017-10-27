===============================
Cookiecutter Django App Package
===============================

Cookiecutter_ template for a Python PyPI ready package library with django app or module, extends upon `wooyek/cookiecutter-pylib`_

Instead of hacking boilerplate setup you can jump to coding immediately. All the check are already in place and a your package can be nicely released to pypi.


* GitHub repo: https://github.com/wooyek/cookiecutter-django-app/
* Documentation: https://cookiecutter-django-app.readthedocs.io/
* Free software: BSD license

.. image:: https://travis-ci.org/wooyek/cookiecutter-django-app.svg
    :target: https://travis-ci.org/wooyek/cookiecutter-django-app
    :alt: Linux build status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/wooyek/cookiecutter-django-app?svg=true
    :target: https://ci.appveyor.com/project/wooyek/cookiecutter-django-app
    :alt: Windows build status on Appveyor

.. image:: https://readthedocs.org/projects/cookiecutter-django-app/badge/?version=latest
    :target: http://cookiecutter-django-app.readthedocs.io/en/latest/
    :alt: Documentation build status


Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``py.test``
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 2.6, 2.7, 3.4, 3.5
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* Bumpversion_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Split file requirements_ management with inheritance and support for private locally installed packages
* Command line interface using Click (optional)
* `Initialization of Git`_ repo, github origin remote and git-flow
* Python `virtual environment bootstrapping`_
* Git master/develop local/origin sync with a single command
* Release_ (sync, test, bump, publish) with a single command

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _requirements: https://github.com/wooyek/cookiecutter-django-app/tree/master/%7B%7Bcookiecutter.project_slug%7D%7D/requirements
.. _Initialization of Git: https://github.com/wooyek/cookiecutter-django-app/blob/master/hooks/post_gen_project.py
.. _virtual environment bootstrapping: https://github.com/wooyek/cookiecutter-django-app/blob/master/hooks/post_gen_project.py
.. _Release: https://github.com/wooyek/cookiecutter-django-app/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/Makefile

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/wooyek/cookiecutter-django-app.git

You'll be prompted for some infomation, based on your choices cookiecutter create a directory that is your new package.
This directory should contain fully initialized project. Empty but passing tests and ready to be pushed and released.

Initial tests and linting should fail on links to your project and documentation returning 404 and unused import in empty modules.
Once you write some code push changes to the repo and setup Read The Docs all should nicely go green.

Post generation provisioning
----------------------------

* Activate virtual environemnt and run tests with ``tox``
* Create a repo on Github (or Bitbucket)
* Add the repo to your Travis-CI_ account.
* Add the repo to your ReadTheDocs_ account + turn on the ReadTheDocs service hook.
* Update `requirements/base.txt` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.

For more details, see the `cookiecutter-django-app tutorial`_.

Running Tests
~~~~~~~~~~~~~

Code has been written, but does it actually work? Let's find out!

::

    source .pyvenv/bin/activate
    (pyvenv) $ pip install -r requirements/local.txt
    (pyvenv) $ pytest
    (pyvenv) $ python setup.py test
    (pyvenv) $ tox


Register releasing on PyPI
~~~~~~~~~~~~~~~~~~~~~~~~~~

First make sure you have newest setuptools installed::

    pip install pip setuptools -U

Once you've got at least a prototype working and tests running,
it's time to register the app on PyPI::

    python setup.py register


Time to release a new version? Bam!

    $ make release

It will sync your local and origin repo, test, increment version number, setup and release package then push to origin master.

.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _Bumpversion: https://github.com/peritus/bumpversion
.. _PyPi: https://pypi.python.org/pypi

.. _`available cookiecutters`: http://cookiecutter.readthedocs.io/en/latest/readme.html#available-cookiecutters
.. _`wooyek/cookiecutter-pylib`: https://github.com/wooyek/cookiecutter-pylib
.. _`ardydedase/cookiecutter-django-app`: https://github.com/ardydedase/cookiecutter-django-app
.. _github comparison view: https://github.com/tony/cookiecutter-django-app-pythonic/compare/audreyr:master...master
.. _`network`: https://github.com/wooyek/cookiecutter-django-app/network
.. _`family tree`: https://github.com/wooyek/cookiecutter-django-app/network/members
.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _`cookiecutter-django-app tutorial`: https://cookiecutter-django-app.readthedocs.io/en/latest/tutorial.html
