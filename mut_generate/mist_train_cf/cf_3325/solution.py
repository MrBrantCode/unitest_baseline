"""
QUESTION:
Write a recursive function `binary_to_decimal` that converts a binary string to its decimal value. The binary string can be up to 16 characters long and may represent a negative number (denoted by a leading '-'). The function should return the decimal equivalent of the input binary string.
"""

def binary_to_decimal(binary):
    if binary.startswith('-'):
        is_negative = True
        binary = binary[1:]
    else:
        is_negative = False

    def helper(binary):
        if len(binary) == 0:
            return 0

        first_digit = int(binary[0])
        remaining_binary = binary[1:]

        result = helper(remaining_binary)
        result = result * 2 + first_digit
        return result

    result = helper(binary)
    if is_negative:
        result = -result
    return result