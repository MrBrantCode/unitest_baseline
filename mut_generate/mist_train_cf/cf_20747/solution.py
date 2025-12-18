"""
QUESTION:
Write a function `average_of_odd_primes` that calculates the average of the sum of all odd prime numbers in a given array. The function should take an array of integers as input and return the average of the sum of the odd prime numbers in the array. The input array can contain duplicate numbers and non-prime numbers.
"""

import math

def average_of_odd_primes(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    odd_prime_nums = [num for num in arr if num % 2 != 0 and is_prime(num)]
    
    if not odd_prime_nums:
        return 0
    
    return sum(odd_prime_nums) / len(odd_prime_nums)