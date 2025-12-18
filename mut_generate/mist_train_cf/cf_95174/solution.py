"""
QUESTION:
Write a function `bytes_to_kilobytes` that takes an integer `bytes` as input, representing a number of bytes between 1 and 1,000,000, and returns the equivalent number of kilobytes. The function must use only bitwise operations and cannot use arithmetic operators or built-in functions.
"""

def bytes_to_kilobytes(bytes):
    kb = bytes >> 10
    return kb