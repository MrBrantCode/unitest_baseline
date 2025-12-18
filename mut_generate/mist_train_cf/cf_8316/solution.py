"""
QUESTION:
Write a function `get_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. The function should have a time complexity of O(n√m), where n is the length of the input list and m is the largest number in the list.
"""

import math

def get_prime_numbers(numbers):
    primes = []
    for num in numbers:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes