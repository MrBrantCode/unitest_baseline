"""
QUESTION:
Write a function named binary_to_decimal that takes a string of binary digits as input and returns the decimal equivalent. The binary number is not guaranteed to be a certain length, but it will only consist of '1's and '0's.
"""

def binary_to_decimal(binary_str):
    return int(binary_str, 2)