"""
QUESTION:
Write a function `binary_representation(number)` that takes an integer `number` as input and returns its binary representation as a string using only bitwise operations. Assume the input integer is a 32-bit signed integer and the output string should be 32 characters long, padding with zeros if necessary.
"""

def binary_representation(number):
    binary = ""
    for i in range(31, -1, -1):
        if number & (1 << i):
            binary += '1'
        else:
            binary += '0'
    return binary