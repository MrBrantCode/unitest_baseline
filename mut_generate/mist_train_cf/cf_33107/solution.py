"""
QUESTION:
Create a function `simulate_lazy_import` that simulates the behavior of the `lazy_import` function. The function should take the module name, symbol, and an optional deprecation version number as input parameters. When the symbol is accessed for the first time, the function should import the module and make it accessible under the specified symbol. If the deprecation version number is provided, the function should issue a deprecation warning when the module is imported. The function should have the following signature: `def simulate_lazy_import(module_name, symbol, deprecation=None):`
"""

import importlib
import warnings

def simulate_lazy_import(module_name, symbol, deprecation=None):
    def lazy_import_wrapper():
        nonlocal module
        if module is None:
            module = importlib.import_module(module_name)
            globals()[symbol] = module

            if deprecation:
                warnings.warn(f"{module_name} is deprecated as of version {deprecation}", DeprecationWarning)

    module = None
    return lazy_import_wrapper