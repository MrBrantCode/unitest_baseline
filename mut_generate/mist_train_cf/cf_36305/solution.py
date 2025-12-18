"""
QUESTION:
Create a function named `count_functions_in_modules` that takes a list of module names as input. The function should return a dictionary where the keys are the module names and the values are the counts of functions defined within each module, excluding built-in functions. If a module cannot be imported, it should be assigned a count of 0 in the dictionary.
"""

import importlib
import inspect

def count_functions_in_modules(module_names):
    function_counts = {}
    for module_name in module_names:
        try:
            module = importlib.import_module(module_name)
            functions = inspect.getmembers(module, inspect.isfunction)
            function_counts[module_name] = len(functions)
        except (ModuleNotFoundError, ImportError):
            function_counts[module_name] = 0
    return function_counts