"""
QUESTION:
Write a function `binary_to_decimal(binary)` that takes a binary string of up to 1000 characters as input and returns its decimal equivalent without using built-in conversion functions or libraries. The function should have a time complexity of O(n), where n is the length of the binary string.
"""

def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1

    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1

    return decimal