"""
QUESTION:
Write a function called `remove_odd_elements` that takes a dictionary as input and returns a new dictionary with all key-value pairs removed where the value is an odd number. The function must preserve the order of the remaining elements.
"""

def remove_odd_elements(input_dict):
    """Remove key-value pairs with odd values from a dictionary, preserving order."""
    return {key: value for key, value in input_dict.items() if value % 2 == 0}