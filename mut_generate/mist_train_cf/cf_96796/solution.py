"""
QUESTION:
Write a function named `unique_prime_numbers` that takes a list of positive integers as input and returns a list of unique prime numbers present in the input list, sorted in ascending order. The function should have a time complexity of O(n√m), where n is the length of the input list and m is the maximum value in the input list.
"""

import math

def unique_prime_numbers(numbers):
    primes = set()
    for num in numbers:
        is_prime = True
        if num <= 1:
            is_prime = False
        else:
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break
        if is_prime:
            primes.add(num)
    return sorted(list(primes))