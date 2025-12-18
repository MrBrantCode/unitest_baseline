"""
QUESTION:
Write a function `extract_keys(dictionary)` that takes a dictionary as input and returns a list of its keys that do not start with 'a' and have string values, including keys from nested dictionaries. The returned list should be sorted in descending order.
"""

def extract_keys(dictionary):
    keys = []

    for key, value in dictionary.items():
        if isinstance(value, dict):
            keys += extract_keys(value)
        elif not key.startswith('a') and isinstance(value, str):
            keys.append(key)

    return sorted(keys, reverse=True)