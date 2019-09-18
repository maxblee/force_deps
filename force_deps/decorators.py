import importlib
import functools


def requires(pkg_name: str):
    """
    *Only* runs a function or initializes a class if a package is available in your environment.

    Parameters
    ----------
    pkg_name
        The name of the required package. This should not be an import as name
        or a module name. For instance, if you need to import pandas, you
        should run `@requires("pandas")`, not `@requires("pd")`.

    Returns
    -------
    This is a decorator that can be run on a function or a class.

    Raises
    ------
    ImportError
        If you cannot import the function (i.e. you have not installed it in
        your current environment)
    ValueError:
        If the package name is not a string
    """
    if not isinstance(pkg_name, str):
        # ignore coverage here because decorators get loaded before with raises test
        # and it's obvious what's happening
        raise TypeError(
            "You must enter a string into this decorator"
        )  # pragma: no cover

    def outer_wrapper(func):
        @functools.wraps(func)
        def run_function(*args, **kwargs):
            if importlib.util.find_spec(pkg_name) is None:
                raise ImportError(
                    "You must import `{}` in order to run `{}`".format(
                        pkg_name, func.__name__
                    )
                )
            return func(*args, **kwargs)

        return run_function

    return outer_wrapper
