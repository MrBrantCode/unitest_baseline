"""
QUESTION:
Write a function named `count_zeros_in_hexadecimal` that takes an integer as input, converts it to a hexadecimal string, and returns the count of '0' characters in the resulting string, excluding any leading '0x' prefix. The function should treat both lowercase and uppercase hexadecimal digits as equivalent, and it should not include any leading zeros in the count.
"""

def count_zeros_in_hexadecimal(num):
    """
    Counts the number of zeros in the hexadecimal representation of a given integer.

    Args:
        num (int): The input integer.

    Returns:
        int: The count of zeros in the hexadecimal representation.
    """
    # Convert to hexadecimal, remove '0x' prefix, and convert to uppercase
    hex_num = hex(num).lstrip("0x").upper()
    
    # Count the number of zeros
    return hex_num.count("0")