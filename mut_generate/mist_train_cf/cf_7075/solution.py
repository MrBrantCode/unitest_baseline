"""
QUESTION:
Write a function `find_missing_prime(numbers)` that takes an array of integers as input and returns the smallest prime number that is not present in the array but is less than or equal to the maximum number in the array. The function should have a time complexity of O(nlogn) and a space complexity of O(1).
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_missing_prime(numbers):
    primes = [num for num in numbers if is_prime(num)]
    for i in range(2, max(numbers) + 1):
        if is_prime(i) and i not in primes:
            return i