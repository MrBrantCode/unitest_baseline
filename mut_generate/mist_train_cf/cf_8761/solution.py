"""
QUESTION:
Create a function `find_smallest_positive_multiple` that takes an array of integers as input and returns the smallest positive number in the array that is a multiple of 3, greater than 5, divisible by 7, and a prime number. If no such number exists, return -1. The function should be able to handle large arrays with up to 10^6 elements efficiently.
"""

import math

def find_smallest_positive_multiple(array):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    return min((num for num in array if num > 5 and num % 3 == 0 and num % 7 == 0 and is_prime(num)), default=-1)