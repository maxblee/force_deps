import subprocess
import pytest
from force_deps import *

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

def test_one_valid_one_invalid_passes_any():
    """If one module is available, `requires_any` is true"""
    @requires_any(["re", "bad_function_name"])
    def returns_none():
        return None
    assert returns_none() is None

def test_one_valid_fails_all():
    @requires_all(["re", "bad_function_name"])
    def returns_none():
        return None
    with pytest.raises(ImportError):
        returns_none()

def test_all_valid_passes_all():
    @requires_all(["re", "itertools"])
    def returns_none():
        return None
    assert returns_none() is None

def test_all_invalid_fails_any():
    """If all modules are unavailable `requires_any` raises error"""
    @requires_any(["bad_function_name", "worse_function_name"])
    def returns_none():
        return None
    with pytest.raises(ImportError):
        returns_none()

def test_single_valid_passes_any():
    """Make sure that `requires_any(string)` == `requires(str)`"""
    @requires_any("re")
    def return_val():
        return 0
    @requires("re")
    def return_zero():
        return 0
    @requires_all("re")
    def return_nothing():
        return 0
    assert return_nothing() == return_val()
    assert return_val() == return_zero()
    assert return_val() == 0

def test_empty_seq_passes_any_and_all():
    """Make sure that `requires_any(empty_list)` is true"""
    @requires_any([])
    def returns_none():
        return None
    @requires_all([])
    def returns_null():
        return None
    assert returns_none() is None
    assert returns_null() is None