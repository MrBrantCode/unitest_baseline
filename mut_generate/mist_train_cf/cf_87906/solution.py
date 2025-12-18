"""
QUESTION:
Write a function `binary_to_decimal(binary)` that takes a string `binary` of at most 16 characters representing a binary number (which may be negative, indicated by a leading '-') and returns its decimal equivalent. Implement the solution using a recursive approach.
"""

def binary_to_decimal(binary):
    if binary.startswith('-'):
        is_negative = True
        binary = binary[1:]
    else:
        is_negative = False

    if len(binary) == 0:
        return 0

    first_digit = int(binary[0])
    remaining_binary = binary[1:]

    result = binary_to_decimal(remaining_binary)
    result = result * 2 + first_digit

    if is_negative:
        result = -result

    return result