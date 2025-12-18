"""
QUESTION:
Write a function `sum_primes(start, end)` that calculates the sum of all prime numbers within a given range (inclusive). The function should take two parameters: `start` and `end`, which define the range. The function should return the sum of all prime numbers in the range.
"""

def is_prime(n):
    if n < 2:
        return False  
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(start, end):
    return sum(num for num in range(start, end+1) if is_prime(num))