"""
QUESTION:
Implement a function named `custom_file_loader` that takes a directory path and a query string as input, and returns a list of Python files in the specified directory that contain the query string in their names.

The function should only consider files with the ".py" extension and ignore subdirectories and files without the ".py" extension. The function should be case-sensitive and return the matching files in the order they are found in the directory.

The input parameters are:
- `directory`: the path to the directory to search for files
- `query_string`: the string to search for in the file names

The output is a list of file names that match the query string.
"""

from typing import List
import os

def custom_file_loader(directory: str, query_string: str) -> List[str]:
    matching_files = []
    for file in os.listdir(directory):
        if file.endswith(".py") and query_string in file:
            matching_files.append(file)
    return matching_files