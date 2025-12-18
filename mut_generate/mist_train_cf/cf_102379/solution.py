"""
QUESTION:
Write a function named `average_odd_primes` that calculates the average of all odd prime numbers in a given array. The function should handle cases where the array is empty or contains no odd prime numbers, returning an error message in such cases. The array can contain both positive and negative integers.
"""

import math

def average_odd_primes(arr):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    odd_primes = [num for num in arr if is_prime(abs(num)) and num % 2 != 0]
    
    if len(odd_primes) == 0:
        return "Error: No odd prime numbers found in the array."
    
    return sum(odd_primes) / len(odd_primes)