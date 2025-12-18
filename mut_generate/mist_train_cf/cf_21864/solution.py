"""
QUESTION:
Write a function `unique_prime_numbers` that takes a list of positive integers as input and returns a list of unique prime numbers present in the input list, sorted in ascending order. The function should have a time complexity of O(n√m), where n is the length of the input list and m is the maximum value in the input list.
"""

import math

def unique_prime_numbers(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    primes = set()
    for num in numbers:
        if is_prime(num):
            primes.add(num)
    return sorted(list(primes))