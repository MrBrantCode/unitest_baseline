"""
QUESTION:
Write a function `sum_of_primes` that takes an array of integers as input and returns the sum of prime numbers in the array. A prime number is a positive integer greater than 1 that is divisible only by itself and 1. The function should not consider integers less than or equal to 1 as prime numbers. Implement the primality test using a more efficient approach. The function should return 0 if there are no prime numbers in the array.
"""

import math

def sum_of_primes(input_array):
    """
    This function calculates the sum of prime numbers in a given array.
    
    Args:
        input_array (list): A list of integers.
    
    Returns:
        int: The sum of prime numbers in the array. Returns 0 if no prime numbers are found.
    """
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    prime_sum = 0
    for num in input_array:
        if is_prime(num):
            prime_sum += num
    return prime_sum