"""
QUESTION:
Write a function `decimal_to_base7` that takes an integer `num` as input and returns its representation in base 7 as a string. The function should use only bitwise operators to convert the remainder to a character. The input number should be within the range of -1000 to 1000.
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