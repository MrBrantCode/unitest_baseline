"""
QUESTION:
Write a function `convert_to_integers` that takes a list of strings as input, where each string represents a floating-point number with an optional negative sign and decimal places. The function should return a new list where each string has been converted to an integer by rounding it to the nearest whole number.
"""

def convert_to_integers(strings):
    """
    This function takes a list of strings representing floating-point numbers 
    and returns a new list with each string converted to an integer by rounding 
    it to the nearest whole number.

    Args:
        strings (list): A list of strings representing floating-point numbers.

    Returns:
        list: A new list with each string converted to an integer.
    """
    return [round(float(string)) for string in strings]