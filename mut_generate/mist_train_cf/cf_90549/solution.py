"""
QUESTION:
Write a function called `filter_keys` that takes a dictionary as input and returns a list of keys whose corresponding values are strings with at least 10 characters. The function should return all matching keys, but should not include keys with non-string or shorter string values.
"""

def filter_keys(dictionary):
    filtered_keys = []
    for key, value in dictionary.items():
        if isinstance(value, str) and len(value) >= 10:
            filtered_keys.append(key)
    return filtered_keys