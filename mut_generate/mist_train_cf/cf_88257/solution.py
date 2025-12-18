"""
QUESTION:
Write a function called `is_prime` that checks if a number is prime and another function to calculate the sum of all prime numbers between 1 and 100,000, excluding palindromic primes. The `is_prime` function should return `True` if a number is prime and `False` otherwise. The sum function should return the sum of all non-palindromic primes in the given range.
"""

def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True