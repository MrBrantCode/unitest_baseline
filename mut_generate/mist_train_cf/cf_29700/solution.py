"""
QUESTION:
Implement a function `load_and_import_module` that takes a directory path and a module name as input, inserts the directory at the beginning of the system path, and imports the specified module from that directory. The function should return the imported module object.
"""

import os
import sys

def load_and_import_module(directory: str, module_name: str) -> object:
    """
    Inserts the specified directory at the beginning of the system path and imports the specified module.

    Args:
    directory: A string representing the directory to be inserted into the system path.
    module_name: A string representing the name of the module to be imported.

    Returns:
    The imported module object.
    """
    # Insert the specified directory at the beginning of the system path
    sys.path.insert(0, directory)

    # Import the specified module
    imported_module = __import__(module_name)

    return imported_module