"""
QUESTION:
Write a function `convert_to_integers` that takes a list of strings as input, where each string represents a floating-point number with an optional negative sign and decimal places, and returns a list of integers. The function should truncate the decimal places and round towards zero when converting the floating-point numbers to integers.
"""

def convert_to_integers(list_of_strings):
    """Convert a list of strings representing floating-point numbers to integers."""
    return [int(float(string)) for string in list_of_strings]