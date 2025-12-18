"""
QUESTION:
Create a function `decimal_to_binary` that takes an integer `num` as input and returns its binary representation as a string, without using the built-in bin() function or any other built-in functions or libraries. The input integer is in base 10 and the output string should be a valid binary number.
"""

def decimal_to_binary(num):
    """
    Convert a decimal number to its binary representation.

    Args:
    num (int): The decimal number to convert.

    Returns:
    str: The binary representation of the input number.
    """
    binary_digits = []
    while num > 0:
        digit = num % 2
        binary_digits.append(digit)
        num = num // 2
    binary_digits.reverse()
    return ''.join(map(str, binary_digits))