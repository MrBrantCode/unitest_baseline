"""
QUESTION:
Create a function named `multiply_prime` that takes a list of integers as input and returns the product of all the prime numbers in the list. If the list does not contain any prime numbers, the function should return `None`. The function should be able to handle lists containing both prime and non-prime numbers.
"""

from math import sqrt
from functools import reduce

def multiply_prime(nums):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    primes = [n for n in nums if is_prime(n)]
    if len(primes) == 0:
        return None
    else:
        return reduce(lambda x, y: x * y, primes)