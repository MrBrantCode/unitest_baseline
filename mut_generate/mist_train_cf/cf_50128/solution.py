"""
QUESTION:
Create a function named `is_fibonacci(n)` that takes an integer `n` as input. The function should return "yes" if `n` is a Fibonacci number and "no" otherwise.
"""

def is_fibonacci(n):
    """Return 'yes' if n is a Fibonacci number, else 'no'."""
    # initialization of the Fibonacci sequence
    a, b = 0, 1

    # Iterate until we've exceeded the number
    while a < n:
        a, b = b, a + b

    # Check if we've actually reached the number
    return 'yes' if a == n else 'no'