"""
QUESTION:
Create a function named `count_file_extensions` that takes a list of filenames as strings and returns a dictionary with unique file extensions (case-insensitive) as keys and their respective counts as values. The function should ignore case sensitivity when comparing file extensions and exclude the dot from the extension.
"""

import os

def count_file_extensions(filenames):
    extension_counts = {}
    for filename in filenames:
        _, ext = os.path.splitext(filename)
        ext = ext.lower()  # Convert the extension to lowercase for case-insensitive comparison
        if ext:
            ext = ext[1:]  # Remove the leading dot from the extension
            extension_counts[ext] = extension_counts.get(ext, 0) + 1
    return extension_counts