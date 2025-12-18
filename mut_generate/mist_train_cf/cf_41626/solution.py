"""
QUESTION:
Write a function `import_subpackages(subpackage_names)` that takes a list of subpackage names as input and returns a dictionary where the keys are the subpackage names and the values are the corresponding imported subpackages as modules. The function should assume that the subpackages are located in the same directory as the main module and have the same names as specified in the `__all__` list. The function should handle cases where a subpackage cannot be imported and return the dictionary with the successfully imported subpackages.
"""

import importlib

def import_subpackages(subpackage_names):
    imported_subpackages = {}
    for subpackage in subpackage_names:
        try:
            imported_subpackages[subpackage] = importlib.import_module(subpackage)
        except ImportError:
            print(f"Error: Subpackage '{subpackage}' not found or unable to import.")
    return imported_subpackages