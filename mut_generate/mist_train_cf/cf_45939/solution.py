"""
QUESTION:
Write a function `primes_in_list` that takes a list of integers as input and returns a list of prime numbers found in the input list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Assume that the input list may not contain five prime numbers. If possible, define a helper function `is_prime` to check if a number is prime.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_list(lst):
    primes = [x for x in lst if is_prime(x)]
    return primes