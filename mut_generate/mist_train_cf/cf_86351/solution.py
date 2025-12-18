"""
QUESTION:
Write a function called `find_prime_index` that takes a sorted array of unique integers as input and returns the index of the first prime number greater than 1,000,000. The array must have at least 10,000 elements and no more than 1,000,000 elements. If there is no prime number greater than 1,000,000 in the array, return -1. The array must not be modified.
"""

import math

def find_prime_index(arr):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(math.sqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    for i in range(len(arr)):
        if arr[i] > 1000000 and is_prime(arr[i]):
            return i
    return -1