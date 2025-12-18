"""
QUESTION:
Create a function named `convert_to_integers` that takes a list of strings as input, where each string represents a floating-point number with optional negative sign and decimal places. The function should return a list of integers where the decimal places of the input numbers are truncated and rounded towards zero.
"""

def convert_to_integers(strings):
    """
    Convert a list of strings representing floating-point numbers to a list of integers.
    
    The decimal places of the input numbers are truncated and rounded towards zero.
    
    Args:
        strings (list): A list of strings representing floating-point numbers.
    
    Returns:
        list: A list of integers.
    """
    return [int(float(string)) for string in strings]