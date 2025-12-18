"""
QUESTION:
Write a function `convert_to_integers` that takes a list of strings representing floating-point numbers with optional negative signs and decimal places. The function should convert each string to a floating-point number, round each positive number to the nearest whole number, and round each negative number down to the nearest whole number. Return the list of converted integers.
"""

def convert_to_integers(list_of_strings):
    """
    Converts a list of strings representing floating-point numbers to a list of integers.
    Positive numbers are rounded to the nearest whole number, while negative numbers are rounded down.

    Args:
        list_of_strings (list): A list of strings representing floating-point numbers.

    Returns:
        list: A list of converted integers.
    """
    return [int(float(string)) if float(string) < 0 else round(float(string)) for string in list_of_strings]