"""
QUESTION:
Write a function `dynamic_import(module_name)` that takes a module name as input and returns the module specification for the given module name, using `importlib` for Python 3.5 and above, and `imp` for Python 2. The function should work correctly for both Python 2 and Python 3.5+.
"""

import sys

def dynamic_import(module_name):
    if sys.version_info >= (3, 5):
        import importlib
        module_spec = importlib.util.find_spec(module_name)
        return module_spec
    else:
        import imp
        module_spec = imp.find_module(module_name)
        return module_spec