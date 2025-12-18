"""
ORIGINAL QUESTION:
Write a function `sum_primes` that takes a list of integers as input and returns the sum of all prime numbers in the list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
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