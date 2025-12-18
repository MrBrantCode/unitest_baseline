"""
QUESTION:
Write a function named `to_octal` that takes an integer as input and returns its octal representation using only bitwise operators. The function should handle both positive and negative numbers and include a negative sign in the output if the input number is negative.
"""

def to_octal(number):
    is_negative = False
    if number < 0:
        is_negative = True
        number = ~number + 1

    octal = ''
    while number > 0:
        octal = str(number & 7) + octal
        number >>= 3

    return '-' + octal if is_negative else octal