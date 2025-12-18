"""
QUESTION:
Write a function `binary_to_decimal(binary)` that takes a binary number as input and returns its decimal equivalent. The function should also include validation to check if the input is a valid binary number, consisting only of 0s and 1s. If the input is not a valid binary number, the function should return an error message.
"""

def binary_to_decimal(binary):
    binary = str(binary)
    if set(binary) == {'0', '1'} or set(binary) == {'0'} or set(binary) == {'1'}:
        return int(binary, 2)
    else:
        return "Error: Invalid binary number. A binary number consists only of 0s and 1s."