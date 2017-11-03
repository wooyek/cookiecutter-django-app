{%- set titile="Welcome to %s's documentation!"|format(cookiecutter.project_name) -%}
{{ titile }}
{% for _ in titile %}={% endfor %}

Contents:

.. toctree::
   :maxdepth: 2

   readme
   installation
   usage
   modules
   contributing
   {% if cookiecutter.create_author_file == 'y' -%}authors
   {% endif -%}history

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
