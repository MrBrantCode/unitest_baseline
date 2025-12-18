"""
QUESTION:
Implement a function named `binary_to_decimal` that takes a string of up to 1000 binary digits (0s and 1s) as input and returns its decimal equivalent without using built-in binary to decimal conversion functions or libraries.
"""

def binary_to_decimal(binary_string):
    decimal = 0
    power = len(binary_string) - 1

    for digit in binary_string:
        decimal += int(digit) * (2 ** power)
        power -= 1

    return decimal