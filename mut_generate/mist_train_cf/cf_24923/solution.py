"""
QUESTION:
Create a function named ConvertToDecimal that takes two parameters: an integer value and its base. The function should convert the given value from its base (between 2 and 16 inclusive) to its decimal representation and return the result. The function should be able to handle any arbitrary number.
"""

def ConvertToDecimal(value, base):
    """
    Converts a given value from its base (between 2 and 16 inclusive) to its decimal representation.

    Args:
        value (int): The value to be converted.
        base (int): The base of the given value.

    Returns:
        int: The decimal representation of the given value.
    """
    decimalValue = 0
    i = 0
    while value != 0:
        remainder = value % 10
        value //= 10
        decimalValue += remainder * (base ** (i))
        i += 1
    return decimalValue