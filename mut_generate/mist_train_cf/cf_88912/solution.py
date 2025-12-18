"""
QUESTION:
Write a function `get_primes(nums)` that takes a list of integers `nums` as input and returns a new list containing only the prime numbers in the input list, sorted in ascending order, with no duplicates. The function should have a time complexity of O(n√m) or better, where n is the length of the input list and m is the maximum value in the input list.
"""

import math

def get_primes(nums):
    primes = []
    for num in nums:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes = list(set(primes))
    primes.sort()
    return primes