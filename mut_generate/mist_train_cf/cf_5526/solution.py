"""
QUESTION:
Write a function `binary_to_decimal(binary)` that takes a binary number as a string and returns its decimal equivalent without using any built-in conversion functions, loops, recursion, or bitwise operators.
"""

def binary_to_decimal(binary):
    if binary == '0':
        return 0
    
    length = len(binary)
    decimal = sum([2**(length - i - 1) for i, bit in enumerate(binary) if bit == '1'])
    
    return decimal