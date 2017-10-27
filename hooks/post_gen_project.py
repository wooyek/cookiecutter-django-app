#!/usr/bin/env python
import os

import shutil
from subprocess import call

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def boostrap_venv():
    print("-------> Bootstrapping virtual environment")
    call(["python3", "-m", "venv", "--clear", ".pyvenv"])
    call([".pyvenv/bin/python", "-m", "pip", "install", "-U", "pip", "setuptools"])
    call([".pyvenv/bin/python", "-m", "pip", "install", "-r", "requirements/local.txt"])


def git_init():
    print("-------> Initializing git repo")
    call(["git", "init"])
    call(["git", "add", "--all"])
    call(["git", "commit", "-am", "init"])
    call(["git", "flow", "init", "-d"])
    call(["git", "remote", "add", "origin", "{{ cookiecutter.repo_url }}.git"])

def remove_example_project():
    location = os.path.join(
        PROJECT_DIRECTORY,
        'example_project'
    )
    shutil.rmtree(location)


if __name__ == '__main__':
    if '{{ cookiecutter.use_pypi_deployment_with_travis }}' != 'y':
        remove_file('travis_pypi_setup.py')

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if '{{ cookiecutter.include_sphinx_doc }}' != 'y':
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, 'docs'))

    if '{{ cookiecutter.git_init }}'.lower() == 'y':
        git_init()

    if '{{ cookiecutter.create_virtual_environment }}'.lower() == 'y':
        boostrap_venv()

    if '{{ cookiecutter.run_tests_on_init }}' == 'y':
        print("-------> Running tests")
        call(["tox"])

    if '{{ cookiecutter.create_example_project }}'.lower() == 'n':
        remove_example_project()

    print(""" 
=============================================================================== 
Hi there, 

as you probably know, creating and maintaining any open source is a massive 
amount of free work. So please spread the word, star any project you use 
and say thank's on twitter to it's authors.

Thx, @wooyek
===============================================================================    
""")
