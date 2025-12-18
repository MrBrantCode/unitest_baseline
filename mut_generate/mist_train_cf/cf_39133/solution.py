"""
QUESTION:
Implement a function `sanitize_invalid_closed_paths(paths)` that takes a list of closed paths as input, where each path is a list of points represented as tuples of two integers, and returns a sanitized list of closed paths. A closed path is considered valid if it has at least 4 points and the first and last points are the same. The function should remove any invalid closed paths from the input list and return the sanitized list.
"""

from typing import List, Tuple

def sanitize_invalid_closed_paths(paths: List[List[Tuple[int, int]]]) -> List[List[Tuple[int, int]]]:
    sanitized_paths = []
    for path in paths:
        if len(path) >= 4 and path[0] == path[-1]:
            sanitized_paths.append(path)
    return sanitized_paths