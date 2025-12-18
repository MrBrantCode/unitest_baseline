"""
QUESTION:
Convert a given number of bytes into kilobytes using only bitwise operations and without using any arithmetic operators or built-in functions. The input is a number of bytes ranging from 1 to 1,000,000, and the conversion should be done in O(1) time complexity. Implement this conversion in a function named `bytes_to_kilobytes`.
"""

def bytes_to_kilobytes(bytes):
    return bytes >> 10