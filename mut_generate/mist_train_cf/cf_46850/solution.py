"""
QUESTION:
Create a function `decimal_to_binary(decimal, precision)` that converts a decimal number to its binary form, handling both integers and floating-point values up to a specified precision. The function should represent negative decimal numbers in two's complement binary form. The precision parameter defaults to 3 if not provided.
"""

def decimal_to_binary(decimal, precision=3):
    # Handling negative decimals using two's complement representation
    if decimal < 0:
        decimal = 2 ** (precision + 1) + decimal

    # Converting the integer part to binary
    integer_part = int(decimal)
    binary_integer = bin(integer_part)[2:]

    # Converting the fractional part to binary
    fractional_part = decimal - integer_part
    binary_fractional = ''
    for _ in range(precision):
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional += str(bit)
        fractional_part -= bit

    if precision > 0:
        binary_result = f'{binary_integer}.{binary_fractional}'
    else:
        binary_result = binary_integer

    return binary_result