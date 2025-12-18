"""
QUESTION:
Write a function called `binary_representation` that takes an integer `number` as input and returns its binary representation as a string, using only bitwise operations. The function should return a 32-bit binary string, padding with zeros on the left if necessary.
"""

def binary_representation(number):
    binary = ""
    for i in range(31, -1, -1):
        if number & (1 << i):
            binary += '1'
        else:
            binary += '0'
    return binary