"""
QUESTION:
Create a function `is_even` and a function `is_odd` that describe whether a number is even or odd using mutual recursion, with the functions calling each other. The functions should return `True` for even numbers and `False` for odd numbers, and should work for all non-negative integers.
"""

def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)