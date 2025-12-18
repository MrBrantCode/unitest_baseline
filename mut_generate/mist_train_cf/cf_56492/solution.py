"""
QUESTION:
Create a function `remove_nulls` that takes a nested dictionary as input and returns the dictionary with all 'null' values removed, including 'null' values within lists and nested dictionaries. The function must preserve the original order of key-value pairs in each dictionary.
"""

def remove_nulls(d):
    if isinstance(d, dict):
        return {k: remove_nulls(v) for k, v in d.items() if v != 'null' and v is not None}
    elif isinstance(d, list):
        return [remove_nulls(v) for v in d if v != 'null' and v is not None]
    else:
        return d