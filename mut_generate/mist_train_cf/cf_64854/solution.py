"""
QUESTION:
Write a function named `has_two_distinct_primes` that takes a list of integers as input and returns a boolean value. The function should return `True` if there are at least two distinct prime numbers in the list, and `False` otherwise. The list may contain negative numbers and zero.
"""

def has_two_distinct_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = set()
    for num in lst:
        if is_prime(abs(num)): # convert to absolute value to handle negative numbers
            primes.add(num)
        if len(primes) >= 2:
            return True
    return False