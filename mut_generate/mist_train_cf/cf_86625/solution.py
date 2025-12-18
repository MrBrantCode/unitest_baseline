"""
QUESTION:
Write a function `sum_primes` that calculates the sum of all prime numbers in a given list of integers. The function should take a list of integers as input and return the sum of all prime numbers in the list. Assume that the input list only contains non-negative integers.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(l):
    return sum([x for x in l if is_prime(x)])