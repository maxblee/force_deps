force-dependencies
==================

| version number: "0.1.0"
| author: Max Lee

|Build Status| |Coverage Status|

Overview
--------

``force-dependencies`` is a small package for enforcing package
requirements at the class- or function-level.

Simply use:

.. code:: python

    from force_deps import requires, requires_any, requires_all

    @requires("sqlalchemy")
    class SQLHandler(object):
        def __init__(self):
            pass

    db = SQLHandler()
    Traceback (most recent call last):
        ...
    ImportError: You must import `sqlalchemy` in order to run `SQLHandler`

to require users to have a package installed in order to use your class
or function,

.. code:: python

    @requires_any(["sqlalchemy", "sqlite3"])
    ...

to require that users have at least one of a number of packages
installed, or

.. code:: python

    @requires_all(["sqlalchemy", "pandas"])
    ...

to require that users have all of a number of packages installed in
order to use a class or function.

Finally, you can combine the decorators together in pretty much any way
you please:

.. code:: python

    @requires_any(["sqlalchemy", "sqlite3"])
    @requires("pandas")
    ...

Installation / Usage
--------------------

| This library requires Python>=3.5. You should be able to extend its
  compatibility by removing the dependencies
| on Python's ``typing`` libraries.

To install use pip:

::

    $ pip install force_deps

Or clone the repo:

.. code:: shell

        $ git clone https://github.com/maxblee/force_deps.git
        $ python setup.py install

.. |Build Status| image:: https://travis-ci.org/maxblee/force_deps.svg?branch=master
   :target: https://travis-ci.org/maxblee/force_deps
.. |Coverage Status| image:: https://coveralls.io/repos/github/maxblee/force_deps/badge.svg?branch=master
   :target: https://coveralls.io/github/maxblee/force_deps?branch=master
