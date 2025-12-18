"""
QUESTION:
Write a function `unique_prime_elements(arr1, arr2)` that takes two arrays of integers as input, combines them, and returns a new array containing only the unique prime numbers in ascending order. The function should achieve a time complexity of O(n log n) and a space complexity of O(n).
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def unique_prime_elements(arr1, arr2):
    unique_elements = set(arr1 + arr2)
    prime_elements = sorted([element for element in unique_elements if is_prime(element)])
    return prime_elements