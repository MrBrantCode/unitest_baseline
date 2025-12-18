"""
QUESTION:
Write a Python function named `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. Then, use this function to iterate over a list of integers, printing out each prime number alongside its original index, and "composite" for each non-prime number.
"""

def is_prime(n):
    """Check if integer n is a prime"""
    if n <= 1:
        return False
    elif n <= 3: 
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True