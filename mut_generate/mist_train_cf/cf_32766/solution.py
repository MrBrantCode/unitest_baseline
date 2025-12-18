"""
QUESTION:
Implement the `_clean_name` function, which takes a string `name` as input and returns the cleaned version of the name, ensuring it is compatible with Windows-style paths. The function should normalize the path and replace backslashes with forward slashes.
"""

import os

def _clean_name(name):
    """
    Cleans the name so that Windows style paths work
    Args:
    name: A string representing the file name

    Returns:
    A string representing the cleaned file name compatible with Windows-style paths
    """
    cleaned_name = os.path.normpath(name).replace('\\', '/')
    return cleaned_name