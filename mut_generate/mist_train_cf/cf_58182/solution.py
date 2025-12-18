"""
QUESTION:
Create a function called `next_fibonacci(n)` that takes a positive integer `n` as input, assuming it is already a part of the standard Fibonacci sequence, and returns the next number in the sequence.
"""

def next_fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        while b <= n:
            a, b = b, a + b
        return b