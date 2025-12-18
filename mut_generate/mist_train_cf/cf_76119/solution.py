"""
QUESTION:
Create a function named `hex_to_octal` that takes a list of hexadecimal numbers as input and returns their equivalent representation in the octal number system. The function should handle hexadecimal numbers of any length and should not include the '0o' prefix in the output.
"""

def hex_to_octal(hex_numbers):
    """
    Convert a list of hexadecimal numbers to their equivalent octal representation.

    Args:
        hex_numbers (list): A list of hexadecimal numbers as strings.

    Returns:
        list: A list of octal numbers as strings.
    """
    return [oct(int(num, 16))[2:] for num in hex_numbers]