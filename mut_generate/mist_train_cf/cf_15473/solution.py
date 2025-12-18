"""
QUESTION:
Write a function `is_prime` that takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. Then, use this function to find all prime numbers between 0 and 1,000,000 and output them in descending order. The function should be efficient enough to handle large ranges.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True