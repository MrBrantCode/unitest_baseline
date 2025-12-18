"""
QUESTION:
Implement a function `excludePaths` that takes a list of file paths as strings and a list of exclusion patterns as strings. The function should return a new list of file paths after excluding any paths that match the exclusion patterns exactly and case-sensitively. The function should exclude a path if any part of the path matches the exclusion pattern.
"""

def excludePaths(file_paths, exclusions):
    return [path for path in file_paths if not any(exclusion in path for exclusion in exclusions)]