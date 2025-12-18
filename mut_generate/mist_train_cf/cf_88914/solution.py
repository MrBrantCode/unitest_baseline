"""
QUESTION:
Write a function `get_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list, with a time complexity of O(n*(log(m))^2), where n is the length of the original list and m is the maximum value in the original list.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_prime_numbers(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes