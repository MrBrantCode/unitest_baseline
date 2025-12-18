"""
QUESTION:
Create a function `find_smallest_prime` that takes a list of positive integers as input and returns the smallest prime number in the list. If no prime number is found, the function should return -1. The function should have a time complexity of O(n√m), where n is the length of the list and m is the largest number in the list. The function should not use any external libraries or functions to check for prime numbers and should only use a constant amount of additional memory space.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_smallest_prime(numbers):
    smallest_prime = -1
    for num in numbers:
        if is_prime(num):
            if smallest_prime == -1 or num < smallest_prime:
                smallest_prime = num
    return smallest_prime