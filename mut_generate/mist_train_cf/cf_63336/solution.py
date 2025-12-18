"""
QUESTION:
Convert the given hexadecimal number to its octal equivalent. Write a function named `hex_to_oct` that takes a hexadecimal string as input and returns the corresponding octal string. The input string should not be prefixed with "0x". The output string should not include the "0o" prefix.
"""

def hex_to_oct(hex_value):
    """
    Converts the given hexadecimal number to its octal equivalent.

    Args:
        hex_value (str): A hexadecimal string without the "0x" prefix.

    Returns:
        str: The corresponding octal string without the "0o" prefix.
    """
    # Convert hexadecimal to decimal
    dec_value = int(hex_value, 16)
    
    # Convert decimal to octal and remove the "0o" prefix
    return oct(dec_value)[2:]