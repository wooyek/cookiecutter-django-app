#!/usr/bin/env python
import os

import shutil
from subprocess import call

import six
import sys
import platform

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def bootstrap_pew(python):
    print("-------> Python Env Wrapper: Bootstrapping virtual environment")
    # delegate all the work to the pew tool
    call((
        "pew", 'new',
        "--python", python,
        '-a', PROJECT_DIRECTORY,
        '-i', 'setuptools',
        '-r', 'requirements/local.txt',
        '--dont-activate',
        '{{ cookiecutter.project_slug }}'
    ))
    return


def bootsrap_pyvenv(python):
    if six.PY2:
        print("-------> VirtualEnv: Bootstrapping virtual environment")
        call(["virtualenv", "--clear", ".pyvenv"])
    else:
        print("-------> PyVenv: Bootstrapping virtual environment")
        call([python, "-m", "venv", "--clear", ".pyvenv"])

    venv_py = ".pyvenv/Scripts/python" if platform.system() == "Windows" else ".pyvenv/bin/python"
    call([venv_py, "-m", "pip", "install", "-U", "pip", "setuptools"])
    call([venv_py, "-m", "pip", "install", "-r", "requirements/local.txt"])


def bootsrap_venv():
    # On Windows  current python3 may just be python or not available from PATH
    python = sys.executable or 'python3'
    if six.PY3 and shutil.which('pew'):
        bootstrap_pew(python)
    else:
        bootsrap_pyvenv(python)


def git_init():
    print("-------> Initializing git repo")
    call(["git", "init"])
    call(["git", "add", "--all"])
    call(["git", "commit", "-am", "init"])
    call(["git", "flow", "init", "-d"])
    call(["git", "remote", "add", "origin", "{{ cookiecutter.repo_url }}.git"])


if __name__ == '__main__':
    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if '{{ cookiecutter.create_virtual_environment }}'.lower() == 'y':
        boostrap_venv()

        if '{{ cookiecutter.include_sphinx_doc }}' == 'y':
            print("-------> Building documentation")
            call(["make", "docs"])

    if '{{ cookiecutter.include_sphinx_doc }}' != 'y':
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, 'docs'))

    if '{{ cookiecutter.run_tests_on_init }}' == 'y':
        print("-------> Running tests")
        call(["tox"])

    if '{{ cookiecutter.create_example_project }}'.lower() == 'n':
        location = os.path.join(PROJECT_DIRECTORY, 'example_project')
        shutil.rmtree(location)

    if '{{ cookiecutter.git_init }}'.lower() == 'y':
        git_init()

    print(""" 
=============================================================================== 
Hi there, 

as you probably know, creating and maintaining any open source is a massive 
amount of free work. So please spread the word, star any project you use 
and say thank's on twitter to it's authors.

Thx, @wooyek
===============================================================================    
""")
    if '{{ cookiecutter.create_virtual_environment }}'.lower() == 'y' and six.PY3 and shutil.which('pew'):
        call(["pew", "workon", "{{ cookiecutter.project_slug }}"])
