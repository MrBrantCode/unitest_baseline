"""
QUESTION:
Write a function `get_highest_prime_with_prime_index` that takes a list of integers as input and returns the highest prime number among all the prime numbers at prime indices (1-indexed) in the list. A prime index refers to the position of a number in the list, starting from 1, that is a prime number. If no such prime number exists, return an appropriate value.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def get_highest_prime_with_prime_index(arr):
    max_prime = float('-inf')
    for i in range(len(arr)):
        if is_prime(i+1) and is_prime(arr[i]) and arr[i] > max_prime:
            max_prime = arr[i]
    return max_prime if max_prime != float('-inf') else None