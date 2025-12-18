"""
QUESTION:
Write a function `add_without_plus` that takes two integers as input and returns their sum without using the "+" operator. The function should have a time complexity of O(log n), where n is the maximum number of bits required to represent the given integers.
"""

def add_without_plus(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x