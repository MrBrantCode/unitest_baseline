"""
QUESTION:
Design a function `decimal_to_binary(number)` that takes an integer or float input between -1000 and 1000 (inclusive) and returns its binary string representation. The function should handle decimal numbers with a fractional part, converting both the integer and fractional parts to binary representation. If the input number is negative, the function should return its two's complement binary representation.
"""

def decimal_to_binary(number):
    # Check if the input is zero
    if number == 0:
        return '0'

    # Handle negative numbers
    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)

    # Separate the integer and fractional parts
    integer_part = int(number)
    fractional_part = number - integer_part

    # Convert the integer part to binary
    binary_integer = ''
    while integer_part > 0:
        remainder = integer_part % 2
        binary_integer += str(remainder)
        integer_part = integer_part // 2

    # Reverse the binary representation string
    binary_integer = binary_integer[::-1]

    # Convert the fractional part to binary
    binary_fractional = ''
    precision = 6  # Maximum precision for the fractional part
    while fractional_part > 0 and precision > 0:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional += str(bit)
        fractional_part -= bit
        precision -= 1

    # Combine the binary integer and fractional parts
    binary_representation = binary_integer
    if binary_fractional:
        binary_representation += '.' + binary_fractional

    # Add the negative sign if applicable
    if is_negative:
        binary_representation = '-' + binary_representation

    return binary_representation