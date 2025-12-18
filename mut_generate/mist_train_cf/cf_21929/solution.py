"""
QUESTION:
Create a function `get_second_largest_prime` that takes an array of integers as input. The function should return the second-largest number that is also a prime number. If there is no second-largest prime number in the array, the function should return -1.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def get_second_largest_prime(numbers):
    prime_numbers = [number for number in numbers if is_prime(number)]
    
    if len(prime_numbers) < 2:
        return -1
    
    return sorted(prime_numbers, reverse=True)[1]