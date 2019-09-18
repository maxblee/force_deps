import subprocess
import pytest
from force_deps.decorators import *

@pytest.mark.parametrize("pkg_name", ["re", "pytest"])
def test_available_function_returns(pkg_name):
    """If a package has been installed in the environment, returns the function"""
    @requires(pkg_name)
    def returns_none():
        return None
    assert returns_none() is None

def test_unavailable_function_raises_error():
    """Makes sure `requires` raises an error if the package has not been installed"""
    @requires("bad_function_name")
    def returns_none():
        return None
    with pytest.raises(ImportError):
        returns_none()

def test_newly_installed_program_runs():
    """Makes sure that after installing (but before importing), requires lets a program run"""
    subprocess.run(["pip", "install", "frozendict"])
    @requires("frozendict")
    def returns_none():
        return None
    try:
        assert returns_none() is None
        # TODO: Clean up this with a better setup/tear down approach
        subprocess.run(["pip", "uninstall", "frozendict", "--yes"])
    except ImportError as err:
        subprocess.run(["pip", "uninstall", "frozendict", "--yes"])
        pytest.fail(err)