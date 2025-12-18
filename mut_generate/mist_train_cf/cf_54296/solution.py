"""
QUESTION:
Write a function `hex_to_decimal` that converts a given hexadecimal number to its equivalent decimal representation without using built-in conversion functions. The input hexadecimal number will be a string and may contain '0x' prefix. The function should handle both lowercase and uppercase letters 'a' to 'f' (representing 10-15 in decimal).
"""

def hex_to_decimal(hex_value):
    """
    Converts a given hexadecimal number to its equivalent decimal representation.

    Args:
        hex_value (str): A string representing a hexadecimal number, possibly with '0x' prefix.

    Returns:
        int: The decimal equivalent of the input hexadecimal number.
    """
    hex_value = hex_value.lstrip("0x")
    decimal_value = 0
    for i in range(len(hex_value)):
        digit_value = 0
        if '0'<= hex_value[i]<= '9':
            digit_value = int(hex_value[i])
        elif 'a'<= hex_value[i]<= 'f':
            digit_value = 10 + ord(hex_value[i]) - ord('a')
        elif 'A'<= hex_value[i]<= 'F':
            digit_value = 10 + ord(hex_value[i]) - ord('A')
        decimal_value += digit_value * (16 ** (len(hex_value) - i - 1))
    return decimal_value