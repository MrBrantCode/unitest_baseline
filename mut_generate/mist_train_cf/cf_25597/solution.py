"""
QUESTION:
Create a function `get_primes` that returns a list of prime numbers within a given range from 2 to `n` (inclusive). The function should take an integer `n` as input and return a list of prime numbers. The function should not take any additional arguments or print any output.
"""

def get_primes(n):
    return [num for num in range(2, n+1) if all(num % i != 0 for i in range(2, num))]