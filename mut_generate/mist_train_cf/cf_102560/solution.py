"""
QUESTION:
Write a function named `filter_keys` that takes a dictionary as input and returns a list of keys. The function should only include keys with string values that contain at least 10 characters.
"""

def filter_keys(dictionary):
    return [key for key, value in dictionary.items() if isinstance(value, str) and len(value) >= 10]