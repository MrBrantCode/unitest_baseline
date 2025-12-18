"""
QUESTION:
Write a Python function `parent_directory_lengths(file_paths)` that takes a list of file paths as input and returns a dictionary where the keys are the parent directories of the file paths and the values are the lengths of the parent directory names. If a file path is a directory itself, consider the directory's parent directory. The function should handle various input scenarios including empty lists, single file paths, multiple file paths with the same parent directory, nested directories, file paths with special characters, and file paths with Unicode characters.
"""

import os

def parent_directory_lengths(file_paths):
    parent_lengths = {}
    for path in file_paths:
        parent_dir = os.path.basename(os.path.dirname(path))
        if parent_dir not in parent_lengths:
            parent_lengths[parent_dir] = len(parent_dir)
    return parent_lengths