"""
QUESTION:
Create a function called `filter_primes` that takes a list of integers as input, removes all prime numbers from the list, sorts the remaining non-prime numbers in ascending order, and returns the sorted list of primes in ascending order and the sum of the remaining non-prime numbers. The function should have a time complexity of O(nlogn) or better.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(arr):
    primes = []
    non_primes_sum = 0
    
    for num in arr:
        if is_prime(num):
            primes.append(num)
        else:
            non_primes_sum += num
    
    primes.sort()
    
    return primes, non_primes_sum