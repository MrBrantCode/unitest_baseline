"""
QUESTION:
Create a function named `binary_to_decimal` that takes a binary string as input and returns its decimal equivalent as an integer. The function should handle invalid binary inputs by returning `None`.
"""

def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        if digit == '1':
            decimal += 2 ** power
        elif digit != '0':
            return None  # Invalid binary number
        power -= 1
    return decimal