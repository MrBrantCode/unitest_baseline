"""
QUESTION:
Write a function `is_even` to determine if a number `n` is even and a function `is_odd` to determine if a number `n` is odd. The functions should use mutual recursion and handle the base cases where `n` is 0. When `n` is not 0, `is_even` should call `is_odd` with `n-1` and `is_odd` should call `is_even` with `n-1`.
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