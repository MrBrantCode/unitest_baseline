"""
QUESTION:
Write a function named `get_max_depth` that takes a nested data structure `data` as input, which can be a dictionary, list, or set containing nested dictionaries, lists, and sets as values. The function should recursively find the maximum depth of the nested data structure.
"""

def get_max_depth(data):
    if isinstance(data, dict):
        return 1 + max((get_max_depth(value) for value in data.values()), default=0)
    elif isinstance(data, (list, set, tuple)):
        return 1 + max((get_max_depth(value) for value in data), default=0)
    else:
        return 1