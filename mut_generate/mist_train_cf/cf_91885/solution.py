"""
QUESTION:
Write a function `extract_keys(dictionary)` that takes a dictionary as input, extracts keys that do not start with 'a' and have string values (including nested dictionaries), and returns them in descending sorted order. The function should handle dictionaries with nested dictionaries as values.
"""

def extract_keys(dictionary):
    keys = []

    for key, value in dictionary.items():
        if isinstance(value, dict):
            keys += extract_keys(value)
        elif not key.startswith('a') and isinstance(value, str):
            keys.append(key)

    return sorted(keys, reverse=True)