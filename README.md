force-dependencies
===============================

version number: "0.1.0"
author: Max Lee

[![Build Status](https://travis-ci.org/<github username>/<repo name>.svg?branch=master)](https://travis-ci.org/<github username>/<repo name>) [![Coverage Status](https://coveralls.io/repos/github/<github username>/<repo name>/badge.svg?branch=master)](https://coveralls.io/github/<github username>/<repo name>?branch=master)

Overview
--------

`force-dependencies` is a small package for enforcing package requirements at the class- or function-level.

Simply use:

```python
from force_deps import requires, requires_any, requires_all

@requires("sqlalchemy")
class SQLHandler(object):
    def __init__(self):
        pass

db = SQLHandler()
Traceback (most recent call last):
    ...
ImportError: You must import `sqlalchemy` in order to run `SQLHandler`
```
to require users to have a package installed in order to use your class or function,

```python
@requires_any(["sqlalchemy", "sqlite3"])
...
```
to require that users have at least one of a number of packages installed, or

```python
@requires_all(["sqlalchemy", "pandas"])
...
```
to require that users have all of a number of packages installed in order to use a class or function.

Finally, you can combine the decorators together in pretty much any way you please:
```python
@requires_any(["sqlalchemy", "sqlite3"])
@requires("pandas")
...
```

Installation / Usage
--------------------

This library requires Python>=3.4.

To install use pip:

    $ pip install force_deps


Or clone the repo:
```shell
    $ git clone https://github.com/maxblee/force_deps.git
    $ python setup.py install
```