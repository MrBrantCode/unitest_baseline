"""
QUESTION:
Write a function `bytes_to_kilobytes` that takes an integer representing the number of bytes as input and returns the equivalent number of kilobytes using only bitwise operations. The function should have a time complexity of O(1) and should not use arithmetic operators or built-in functions. The input range of bytes is 1 to 1,000,000.
"""

def bytes_to_kilobytes(bytes):
    return bytes >> 10