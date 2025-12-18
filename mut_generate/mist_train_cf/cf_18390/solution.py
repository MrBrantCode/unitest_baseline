"""
QUESTION:
Write a function named `bytes_to_kilobytes` that takes one argument, `bytes`, representing a number of bytes between 1 and 1,000,000, and returns the equivalent number of kilobytes using only bitwise operations without any arithmetic operators or built-in functions. The input `bytes` is a non-negative integer.
"""

def entance(bytes):
    kb = bytes >> 10
    return kb