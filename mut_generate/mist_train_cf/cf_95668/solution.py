"""
QUESTION:
Write a function `convert_number` that takes three parameters: a positive integer `number`, the `base` of the number, and the `target_base`. The function should convert the given `number` from the given `base` to the `target_base` and return the converted number as a string. The function should handle converting numbers up to 10^18. The `base` and `target_base` should be in the range of 2 to 36. Do not use any built-in functions or libraries that directly solve the problem.
"""

def convert_number(number, base, target_base):
    if number == 0:
        return '0'

    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    converted_number = ''

    while number > 0:
        remainder = number % target_base
        if remainder < 10:
            converted_number += str(remainder)
        else:
            converted_number += digits[remainder]
        number //= target_base

    return converted_number[::-1]