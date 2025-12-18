"""
QUESTION:
Write a function `unique_prime_elements(arr1, arr2)` that takes two arrays of integers as input, and returns a sorted array of unique prime numbers from both arrays. The function should have a time complexity of O(n log n) and a space complexity of O(n).
"""

import math

def unique_prime_elements(arr1, arr2):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    unique_elements = set(arr1 + arr2)
    prime_elements = [element for element in unique_elements if is_prime(element)]
    prime_elements.sort()
    return prime_elements