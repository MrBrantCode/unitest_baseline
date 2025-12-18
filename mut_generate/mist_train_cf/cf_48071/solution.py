"""
QUESTION:
Write a function named `sum_of_sq_root` that calculates the sum of the square roots of unique non-negative integers from an array, disregarding zero and non-integer values. The function should return the sum of the square roots of unique positive numbers in the array, zero if there are no such numbers, and `None` if the array is empty. The function should also accept optional parameters `primes_only` and `reverse` to consider only prime numbers and calculate the sum of square roots in reverse order of the array respectively.
"""

import math

def sum_of_sq_root(arr: list, primes_only: bool = False, reverse: bool = False) -> float:
    if not arr: return None
    filtered_arr = [i for i in set(arr) if isinstance(i, int) and i > 0]
    if primes_only:
        filtered_arr = [i for i in filtered_arr if is_prime(i)]
    if reverse:
        filtered_arr.sort(reverse = True)
    return sum(math.sqrt(i) for i in filtered_arr)

def is_prime(n: int) -> bool: 
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True