"""
QUESTION:
Write a function `count_files_by_extension` that takes in a list of absolute file paths and an extension, and returns the count of files with the given extension in the entire directory structure. The function should consider the extension case-insensitive. The file paths are guaranteed to be valid absolute paths in the directory structure. The length of the list of file paths is between 1 and 10^4, and the length of the extension is between 1 and 10.
"""

from typing import List

def count_files_by_extension(file_paths: List[str], extension: str) -> int:
    count = 0
    for path in file_paths:
        if path.lower().endswith("." + extension.lower()):
            count += 1
    return count