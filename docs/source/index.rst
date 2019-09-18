Welcome to force-dependencies's documentation!
==============================================

`force-dependencies` is a lightweight tool for ensuring that users have the right dependencies
before they run functions or classes that depend on them.

The module is particularly aimed at programs with extensible features and at
programs that have convenience return methods.

Say, for instance, that you are writing a library to help people deserialize and serialize data.
You may want to help users serialize and deserialize into a wide variety of data: from
geospatial data to JSON to SQL databases. Pretty soon, your library could become far too bulky
for someone who just wants some convenient methods to convert strings into integers.

With `force-dependencies`, you can easily manage those dependencies. For a SQL deserialization
class, for instance, you could require that users have `sqlalchemy` installed. When users who
haven't installed `sqlalchemy` in their current environment try to initialize the class, they will
receive an error:

    >>> from force_deps import requires
    >>> @requires("sqlalchemy")
    ... class SQLHandler(object):
    ...     def __init__(self):
    ...         pass
    >>> db = SQLHandler()
    Traceback (most recent call last):
        ...
    ImportError: You must import `sqlalchemy` in order to run `SQLHandler`

Alternatively, you could allow users to optionally use `sqlalchemy` or Python's built-in `sqlite3` module,
allowing users to avoid downloading `sqlalchemy` if they want to:

    >>> from force_deps import requires_any
    >>> @requires_any("sqlalchemy", "sqlite3")
    ... class SQLHandler(object):
    ...     def __init__(self, data):
    ...         self.data = data
    >>> db = SQLHandler([])
    >>> self.data
    []

Or, finally, you could require that users have installed several dependencies:

    >>> from force_deps import requires_all
    >>> @requires_all("sqlite3", "pandas")
    ... class SQLHandler(object):
    ...     def __init__(self, data):
    ...         self.data = data
    >>> db = SQLHandler([])
    Traceback (most recent call last):
        ...
    ImportError: You must import `sqlalchemy` in order to run `SQLHandler`

(This is equivalent to running):

    >>> from force_deps import requires
    >>> @requires("sqlite3")
    >>> @requires("pandas")
    ... class SQLHandler(object):
    ...     def __init__(self, data):
    ...         self.data = data
    >>> db = SQLHandler([])
    Traceback (most recent call last):
        ...
    ImportError: You must import `sqlalchemy` in order to run `SQLHandler`

The entire library is just those three decorators, but I think it can frequently come in handy,
particularly when you're writing a library that you want to be extensible and flexible for users.

As one final example, the decorators in this library can come in handy for simple data output functions.
For instance, you could easily create a function to output data from an object into a `pandas DataFrame`
without requiring anyone to install pandas. 

Simply type:

>>> from force_deps import requires
>>> class DataHandler(object):
...     def __init__(self, data):
...         self.data = data
...     @requires("pandas")
...     def to_sql(self):
...         import pandas as pd
...         return pd.DataFrame(self.data)

API
===

.. automodule:: force_deps
    :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

