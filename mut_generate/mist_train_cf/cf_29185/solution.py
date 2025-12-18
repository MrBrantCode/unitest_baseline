"""
QUESTION:
Write a function `longest_common_prefix(file_paths)` that takes a list of absolute file paths as input and returns the longest common prefix among them. Each file path consists of alphanumeric characters and slashes, and starts with a slash. The input list will have at least one element.
"""

from typing import List

def longest_common_prefix(file_paths: List[str]) -> str:
    if not file_paths:
        return ""

    min_len = min(len(path) for path in file_paths)
    prefix = ""
    for i in range(min_len):
        char = file_paths[0][i]
        if all(path[i] == char for path in file_paths):
            prefix += char
        else:
            break
    return prefix