"""
QUESTION:
Write a function named `convert_base_10_to_base_8` that takes an integer `number` in base 10 as input and returns its equivalent in base 8 as a string.
"""

def convert_base_10_to_base_8(number):
    binary_number = bin(number)[2:]
    octal_number = oct(int(binary_number, 2))[2:]
    return octal_number