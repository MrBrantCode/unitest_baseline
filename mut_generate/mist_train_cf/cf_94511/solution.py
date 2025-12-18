"""
QUESTION:
Create a function named `to_octal` that takes an integer `num` as input and returns its octal representation using only bitwise operators. The function should be able to handle both positive and negative integers within the range of a 32-bit signed integer. The output should be an integer representing the octal value, with a negative sign if the input is negative.
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