"""
QUESTION:
Write a function `count_prime_numbers` that takes an array of integers as input and returns the count of prime numbers in the array. The function should handle arrays of any length and contain both positive and non-positive integers.
"""

import math

def count_prime_numbers(arr):
    def is_prime(num):
        if num < 2:  
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:  
                return False
        return True

    count = 0
    for num in arr:
        if is_prime(num):
            count += 1
    return count