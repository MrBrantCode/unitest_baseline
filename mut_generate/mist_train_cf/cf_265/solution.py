"""
QUESTION:
Find the index of the first prime number greater than 1,000,000 in a given sorted array of unique integers. The array must contain between 10,000 and 1,000,000 elements. The index must be returned as a positive integer. If no prime number greater than 1,000,000 exists in the array, return -1. The array must not be modified. Implement the function `find_prime_index(arr)`.
"""

import math

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

def find_prime_index(arr):
    for i in range(len(arr)):
        if arr[i] > 1000000 and is_prime(arr[i]):
            return i
    return -1