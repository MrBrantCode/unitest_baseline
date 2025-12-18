"""
QUESTION:
Implement the function `decimal_to_hexadecimal(num: int) -> str` to convert a decimal number to its hexadecimal representation. The function should take an integer `num` as input and return its hexadecimal representation as a string. The input `num` will be within the range of -2^31 to 2^31 - 1. Do not use any built-in functions or libraries for conversion.
"""

def decimal_to_hexadecimal(num: int) -> str:
    """
    Convert a decimal number to its hexadecimal representation.

    Args:
    num (int): The decimal number to be converted.

    Returns:
    str: The hexadecimal representation of the input number.

    """
    if num == 0:
        return '0'
    if num < 0:
        return '-' + decimal_to_hexadecimal(-num)
    hex_map = "0123456789ABCDEF"
    hex_str = ""
    while num > 0:
        remainder = num % 16
        hex_str = hex_map[remainder] + hex_str
        num = num // 16
    return hex_str