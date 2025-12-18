"""
QUESTION:
Implement a function `count_unique_extensions` that takes a list of file paths as input and returns a dictionary containing the count of files with unique extensions. The function should ignore case sensitivity when comparing file extensions. The file extension is considered unique if it has a different name, regardless of its case (e.g., '.txt' and '.TXT' are considered the same extension).

The function should return a dictionary where the keys are the unique file extensions (in lowercase) and the values are the corresponding counts. The function should handle file paths with different operating system conventions (e.g., forward slashes, backslashes).
"""

from typing import List, Dict
import os

def count_unique_extensions(file_paths: List[str]) -> Dict[str, int]:
    extension_counts = {}
    for file_path in file_paths:
        _, file_extension = os.path.splitext(file_path)
        file_extension = file_extension.lower()  # Convert to lowercase for case-insensitive comparison
        if file_extension not in extension_counts:
            extension_counts[file_extension] = 1
        else:
            extension_counts[file_extension] += 1
    return extension_counts