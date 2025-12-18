"""
QUESTION:
Write a function named `largest_prime_number` that takes an array of integers as input and returns the largest prime number in the array. If no prime number is found, the function should return `None`. The input array can contain any integer values (positive, negative, or zero). The function should handle these cases accordingly.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def largest_prime_number(array):
    largest_prime = None
    for num in array:
        if is_prime(num):
            if largest_prime is None or num > largest_prime:
                largest_prime = num
    return largest_prime