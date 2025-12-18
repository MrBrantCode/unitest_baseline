"""
QUESTION:
Write a function `is_prime_with_prime_index(arr)` to determine whether a prime number with a prime index is present in the given array. The function should return `True` if such a number exists and `False` otherwise. The array index starts at 0.
"""

import math

def is_prime_with_prime_index(arr):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    prime_indexes = [i for i in range(len(arr)) if is_prime(i)]
    prime_numbers = [arr[i] for i in prime_indexes]
    for num in prime_numbers:
        if is_prime(num):
            return True
    return False