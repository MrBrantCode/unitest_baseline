"""
QUESTION:
Write a function `count_primes` that takes an array of integers as input and returns the number of prime numbers in the array. The function should have a time complexity of O(n * sqrt(m)), where n is the length of the array and m is the maximum value in the array.
"""

import math

def count_primes(arr):
    count = 0
    for num in arr:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count