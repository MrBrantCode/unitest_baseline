"""
QUESTION:
Implement a function called `binary_to_decimal` that takes a binary string as input and returns its decimal equivalent. The input string is up to 1000 characters long, contains only 0s and 1s, and should be converted without using built-in functions or libraries for binary-to-decimal conversion.
"""

def binary_to_decimal(binary_string):
    decimal = 0
    power = len(binary_string) - 1

    for digit in binary_string:
        decimal += int(digit) * (2 ** power)
        power -= 1

    return decimal