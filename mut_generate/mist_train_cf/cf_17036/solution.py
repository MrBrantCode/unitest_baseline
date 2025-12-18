"""
QUESTION:
Write a function `to_octal(num)` that takes an integer `num` and returns its octal representation as an integer. The function should handle both positive and negative numbers, and only use bitwise operators for the conversion.
"""

def to_octal(num):
    if num == 0:
        return 0

    negative = False
    if num < 0:
        negative = True
        num = -num

    result = 0
    power = 1

    while num > 0:
        result += (num & 0b111) * power
        num >>= 3
        power *= 10

    if negative:
        result = -result

    return result