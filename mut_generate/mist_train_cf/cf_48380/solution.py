"""
QUESTION:
Convert the given integer into its corresponding binary categorization using Python. The function should be named `decimal_to_binary` and take an integer as input. The function should return a string representing the binary number without the '0b' prefix. The function must not use Python's built-in `bin()` function.
"""

def decimal_to_binary(n):
    """
    Converts an integer into its binary representation.

    Args:
        n (int): The decimal number to be converted.

    Returns:
        str: A string representing the binary number without the '0b' prefix.
    """
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary