"""
QUESTION:
Write a function `find_nested_key(d, nested_key)` that returns the value of `nested_key` in a deeply nested dictionary `d` of unknown depth and structure. If `nested_key` does not exist in the dictionary, return `None`.
"""

def find_nested_key(d, nested_key):
    if nested_key in d:
        return d[nested_key]
    for k, v in d.items():
        if isinstance(v, dict):
            result = find_nested_key(v, nested_key)
            if result is not None:
                return result
    return None