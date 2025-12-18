"""
QUESTION:
Process a list of file paths by ignoring paths that start with '-i' and expanding the rest using glob patterns. Write a function `process_file_paths` that takes a list of file paths as input and returns the expanded file paths.
"""

import glob

def process_file_paths(file_paths):
    expanded_paths = []
    for path in file_paths:
        if path.startswith("-i"):
            continue  # Ignore the file path
        else:
            expanded_paths.extend(glob.glob(path))  # Expand the file path pattern

    return expanded_paths