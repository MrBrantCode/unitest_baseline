"""
QUESTION:
Create a function called `reload_module` that takes no parameters and reloads a Python module in a Jupyter environment to reflect changes made to the module's file after the initial import, and explain how to handle the similar issue of reading updated text or CSV files. Ensure the function uses the `importlib` library.
"""

import importlib

def reload_module(module_name):
    """
    Reloads a Python module in a Jupyter environment.

    Args:
    module_name (str): The name of the module you want to reload.
    """
    module = importlib.import_module(module_name)
    return importlib.reload(module)