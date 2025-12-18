"""
QUESTION:
Design a function `is_prime` that takes an integer `n` as input and returns a boolean indicating whether `n` is a prime number. Then, use this function to generate a list of all prime integers between 500 and 1000 (inclusive). The function should be efficient and transparent in its methodology for identifying prime numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True