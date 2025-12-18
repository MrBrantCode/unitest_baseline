"""
QUESTION:
Write a function `find_combinations` that takes an array of integers as input and returns all combinations of 3 distinct prime numbers in the array that sum to zero. The function should consider only the prime numbers in the input array.
"""

import itertools

def find_combinations(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [num for num in arr if is_prime(num)]
    combinations = list(itertools.combinations(primes, 3))
    return [combo for combo in combinations if sum(combo) == 0]