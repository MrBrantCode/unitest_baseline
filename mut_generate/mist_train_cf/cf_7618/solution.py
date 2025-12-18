"""
QUESTION:
Write a function `decimal_to_hexadecimal(num: int) -> str` that takes an integer `num` within the range of -2^63 to 2^63 - 1 and returns its hexadecimal representation as a string without using any built-in functions or libraries for conversion.
"""

def decimal_to_hexadecimal(num: int) -> str:
    """
    This function converts a decimal number to its hexadecimal representation.

    Args:
        num (int): The decimal number to be converted.

    Returns:
        str: The hexadecimal representation of the decimal number.
    """

    hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    # Initialize an empty string to store the hexadecimal representation
    hex_str = ''

    # If the input number is 0, return '0' as the hexadecimal representation
    if num == 0:
        return '0'

    # If the input number is negative, append a '-' to the hexadecimal representation and take the absolute value of the number
    if num < 0:
        sign = '-'
        num = -num
    else:
        sign = ''

    # While the number is greater than 0
    while num > 0:
        # Take the remainder of the number divided by 16
        remainder = num % 16

        # If the remainder is less than 10, append it as a character to the hexadecimal representation
        if remainder < 10:
            hex_str = str(remainder) + hex_str
        # If the remainder is greater than or equal to 10, append the corresponding uppercase letter to the hexadecimal representation
        else:
            hex_str = hex_map[remainder] + hex_str

        # Divide the number by 16
        num = num // 16

    # Return the hexadecimal representation with the sign
    return sign + hex_str