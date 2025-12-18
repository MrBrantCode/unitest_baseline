"""
QUESTION:
Write a function `find_twin_primes` that takes one argument, `num_pairs`, and returns a list of the first `num_pairs` twin prime pairs. A twin prime pair is a pair of prime numbers with a difference of 2. The function should also be able to calculate the standard deviation of these pairs in an efficient way. The solution should minimize both time and space complexity.
"""

import numpy as np

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n%i == 0 or n%(i + 2) == 0:
            return False
        i += 6
    return True

def find_twin_primes(num_pairs):
    prime_pairs = []
    current = 2
    while len(prime_pairs) < num_pairs:
        if is_prime(current) and is_prime(current + 2):
            prime_pairs.append((current, current + 2))
        current += 1
    flat_list = [num for pair in prime_pairs for num in pair]
    return prime_pairs, np.std(flat_list)