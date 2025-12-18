"""
QUESTION:
Write a function named `sort_dict_by_value` that takes a dictionary as input and returns a new dictionary with the same key-value pairs sorted by the dictionary's values in ascending order. Assume the input dictionary's values are comparable (e.g., all integers or all strings).
"""

def sort_dict_by_value(input_dict):
    """Sorts a dictionary by its values in ascending order."""
    return {k: v for k, v in sorted(input_dict.items(), key=lambda item: item[1])}