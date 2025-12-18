"""
QUESTION:
Write a function `nth_fibonacci_number(n)` that returns the value at index `n` in the Fibonacci sequence, where the sequence starts with 0 and 1. The function should handle integers `n` greater than or equal to 0.
"""

def nth_fibonacci_number(n):
    """Find the value of n where n is the index of the Fibonacci Sequence."""
    if n < 2:
        return n 
    elif n == 2:
        return 1
    else:
        return nth_fibonacci_number(n-1) + nth_fibonacci_number(n-2)