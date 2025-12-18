"""
QUESTION:
Write a function named `contains_prime` that takes a list of integers as input and returns `True` if any number in the list is a prime number, and `False` otherwise. The list can contain both positive and negative integers. The function should have a time complexity of O(n * sqrt(m)), where n is the length of the list and m is the maximum absolute value in the list. Minimize the space complexity of the solution.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def contains_prime(numbers):
    for num in numbers:
        if is_prime(abs(num)):
            return True
    return False