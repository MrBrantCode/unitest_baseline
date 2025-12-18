"""
QUESTION:
Write a function called `is_even_or_odd` that takes a 64-bit integer as input and returns whether the number is "Even" or "Odd" without using any arithmetic or comparison operators. The function should work correctly for both positive and negative integers.
"""

def is_even_or_odd(num):
    if num & 1:  # Bitwise AND with 1
        return "Odd"
    else:
        return "Even"