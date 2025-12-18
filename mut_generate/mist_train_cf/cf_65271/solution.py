"""
QUESTION:
Implement a function using mutual recursion to determine whether a number is even or odd. The function should take an integer `n` as input and return `True` if `n` is even and `False` if `n` is odd. Use two separate functions, `is_even` and `is_odd`, that call each other recursively until the base case is met. Ensure the recursion ends when `n` becomes 0.
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