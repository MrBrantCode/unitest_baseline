"""
QUESTION:
Create a function `find_third_largest_prime` that takes an array of integers as input. The function should return the third-largest prime number in the array. If there are less than three prime numbers in the array, return -1. 

The function should use a helper function `is_prime` to check if a number is prime. The `is_prime` function should return True if a number is prime and False otherwise. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The `is_prime` function should check divisibility from 2 to the square root of the number (rounded up).
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, math.isqrt(num)+1):
        if num % i == 0:
            return False
    return True

def find_third_largest_prime(arr):
    prime_numbers = [num for num in arr if is_prime(num)]
    return -1 if len(prime_numbers) < 3 else sorted(prime_numbers, reverse=True)[2]