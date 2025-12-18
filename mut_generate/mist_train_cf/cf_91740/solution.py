"""
QUESTION:
Write a function `hex_to_binary` that takes a hexadecimal number as a string as input and returns its binary representation as a string using bitwise operators without any built-in conversion functions. The function should handle hexadecimal numbers from '0' to 'F' and the output should be a string of 4*n binary digits where n is the number of hexadecimal digits in the input.
"""

def hex_to_binary(hex_num):
    """
    Converts a hexadecimal number to its binary representation using bitwise operators.

    Args:
    hex_num (str): A hexadecimal number as a string.

    Returns:
    str: The binary representation of the input hexadecimal number.
    """
    hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    binary = ''
    for char in hex_num.upper():
        binary += hex_to_bin[char]
    return binary