"""
QUESTION:
Implement a function `list_non_private_modules(package_name)` that takes the name of a package as a string and returns a list of non-private modules (i.e., modules not starting with an underscore) within that package. The function should not use any external libraries other than those provided in the Python standard library.
"""

import importlib
import pkgutil
import os

def list_non_private_modules(package_name):
    package_path = os.path.dirname(__import__(package_name).__file__)
    modules = [name for _, name, _ in pkgutil.iter_modules([package_path])]
    non_private_modules = [module for module in modules if not module.startswith('_')]
    return non_private_modules