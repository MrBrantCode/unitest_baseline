"""
QUESTION:
Write a function named `decimal_to_hexadecimal` that takes an integer `decimal` as input and returns its hexadecimal representation as a string. The function should handle decimal numbers between -1000 and 1000 inclusive, and print an error message if the input is outside this range. Negative decimal numbers should be converted to their sign-magnitude hexadecimal representation.
"""

def decimal_to_hexadecimal(decimal):
    """
    Converts a decimal number to its hexadecimal representation.

    Args:
    decimal (int): The decimal number to convert. Must be between -1000 and 1000.

    Returns:
    str: The hexadecimal representation of the decimal number as a string.

    """
    if decimal < -1000 or decimal > 1000:
        print("Error: Decimal number must be between -1000 and 1000")
        return

    if decimal < 0:
        decimal = abs(decimal)
        sign = "-"
    else:
        sign = ""

    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        decimal //= 16

    if hexadecimal == "":
        hexadecimal = "0"

    return sign + hexadecimal