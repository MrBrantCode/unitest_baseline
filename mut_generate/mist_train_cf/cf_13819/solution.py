"""
QUESTION:
Write a function named `find_max_binary_value` that takes a list of binary strings as input, converts each binary string into an integer, and returns the maximum integer value. The function should assume that all input binary strings are valid and can be converted to integers.
"""

def find_max_binary_value(binary_strings):
    """
    Converts a list of binary strings into integers and returns the maximum integer value.

    Args:
        binary_strings (list): A list of binary strings.

    Returns:
        int: The maximum integer value.
    """
    return max(int(binary_string, 2) for binary_string in binary_strings)