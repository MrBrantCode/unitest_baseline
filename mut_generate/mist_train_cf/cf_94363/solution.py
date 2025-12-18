"""
QUESTION:
Write a function `get_permutations(chars)` that takes a list of integers as input and returns all possible permutations of the input list where each permutation only contains prime numbers and the sum of these prime numbers is also a prime number.
"""

import itertools

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_sum_prime(prime_list):
    prime_sum = sum(prime_list)
    return is_prime(prime_sum)

def get_permutations(chars):
    primes = []
    for perm in itertools.permutations(chars):
        prime_perm = [x for x in perm if is_prime(x)]
        if is_sum_prime(prime_perm):
            primes.append(prime_perm)
    return primes