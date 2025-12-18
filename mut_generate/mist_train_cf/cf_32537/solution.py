"""
QUESTION:
Create a function named `filter_file_paths` that takes a list of file paths, an inclusion pattern, and a list of exclusion patterns. The function should return a list of file paths that match the inclusion pattern but do not match any of the exclusion patterns. The inclusion and exclusion patterns may be in the form of Unix shell-style wildcards. If the inclusion pattern contains multiple patterns, they should be comma-separated. The function should use the `fnmatch` module to match file paths against the patterns.
"""

from typing import List
import fnmatch

def filter_file_paths(file_paths: List[str], include: str, omit: List[str]) -> List[str]:
    included_files = []
    for file_path in file_paths:
        if any(fnmatch.fnmatch(file_path, pattern) for pattern in include.split(',')):
            if not any(fnmatch.fnmatch(file_path, pattern) for pattern in omit):
                included_files.append(file_path)
    return included_files