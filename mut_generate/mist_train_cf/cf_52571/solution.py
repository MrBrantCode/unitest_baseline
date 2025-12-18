"""
QUESTION:
Create a function called `binary_to_decimal` that takes a string of binary digits as input and returns its equivalent decimal value. The function should use the built-in `int()` function with base 2. Assume the input string only contains binary digits (0 and 1) and does not contain any error handling for non-binary inputs.
"""

def binary_to_decimal(binary_string):
    # Using int() function to convert binary to decimal
    return int(binary_string, 2)