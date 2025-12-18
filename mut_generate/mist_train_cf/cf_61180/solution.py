"""
QUESTION:
Develop a function named `find_path` that takes two parameters: a multi-dimensional numerical array (nested up to 3 levels deep) and a target integer `x`. The function should return the path to the target integer as an array of indices if found, or `None` otherwise. The array is 0-indexed.
"""

def find_path(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return [i]
        if isinstance(arr[i], list):
            path = find_path(arr[i], x)
            if path is not None:
                return [i] + path
    return None