"""
QUESTION:
Write a function named `get_prime_numbers` that takes a list of numbers as input and returns a new list containing only the prime numbers from the original list. The function should have a time complexity of O(n√m), where n is the length of the input list and m is the largest number in the list.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_numbers(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes