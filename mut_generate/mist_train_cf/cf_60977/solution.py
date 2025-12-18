"""
QUESTION:
Write a function named `is_even` and `is_odd` to determine whether a number is even or odd using mutual recursion, with the constraint that the function should handle integer inputs and use a recursive approach.
"""

def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)