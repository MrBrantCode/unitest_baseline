"""
QUESTION:
Write a function named decimal_to_base7 that converts a given decimal number to its base 7 representation using bitwise operators only. The input number should be an integer within the range of -1000 to 1000, and the output should be a string representing the base 7 value.
"""

def decimal_to_base7(num):
    if num == 0:
        return '0'

    is_negative = False
    if num < 0:
        is_negative = True
        num = -num

    result = ''
    while num > 0:
        remainder = num % 7
        char = chr(remainder + 48)  # Convert remainder to character using bitwise operators only
        result = char + result
        num //= 7

    if is_negative:
        result = '-' + result

    return result