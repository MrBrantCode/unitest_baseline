"""
QUESTION:
Create a function `filter_primes` that takes an array of integers as input and returns a tuple containing a sorted list of prime numbers in ascending order and the product of all non-prime numbers in the array. The function should have a time complexity of O(nlogn) or better.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def filter_primes(arr):
    primes = []
    non_primes_product = 1
    for num in arr:
        if is_prime(num):
            primes.append(num)
        else:
            non_primes_product *= num
    primes.sort()
    return primes, non_primes_product