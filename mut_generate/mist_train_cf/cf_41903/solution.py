"""
QUESTION:
Implement a function `has_valid_extension(path)` that takes a file path as input and returns True if the file has an extension that matches any of the extensions listed in the PATHEXT variable, and False otherwise. The function should be case-insensitive when comparing file extensions, consider a file path without an extension (i.e., no period '.' in the file name) as invalid, and use the environment variables for the list of valid extensions.
"""

import os

def has_valid_extension(path):
    _, file_extension = os.path.splitext(path)
    if file_extension:
        valid_extensions = [ext.lower() for ext in os.environ['PATHEXT'].split(os.pathsep)]
        return file_extension.lower() in valid_extensions
    else:
        return False