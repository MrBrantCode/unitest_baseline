"""
QUESTION:
Write a function `find_largest_prime` that takes a list of numbers as input and returns the largest prime number in the list. If no prime numbers are found, return -1. The input list can contain integers and/or floats, but prime numbers are defined as natural numbers greater than 1 that are divisible only by 1 and themselves.
"""

import math

def find_largest_prime(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    largest_prime = -1
    for num in numbers:
        if isinstance(num, int) and is_prime(num) and num > largest_prime:
            largest_prime = num
    return largest_prime