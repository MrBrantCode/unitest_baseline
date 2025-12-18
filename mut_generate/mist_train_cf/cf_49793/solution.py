"""
QUESTION:
Write a function called `string_to_hex` that takes an input string and returns its hexadecimal representation. The input string should be encoded into bytes using UTF-8 before converting to hexadecimal.
"""

def string_to_hex(input_string):
    """
    This function takes an input string and returns its hexadecimal representation.
    The input string is encoded into bytes using UTF-8 before converting to hexadecimal.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: The hexadecimal representation of the input string.
    """
    return input_string.encode("utf-8").hex()