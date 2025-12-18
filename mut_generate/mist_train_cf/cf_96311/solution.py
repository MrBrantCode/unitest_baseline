"""
QUESTION:
Write a function named `find_largest_prime` that takes an array of numbers as input and returns the largest prime number in the array. If there are no prime numbers in the array, return -1. A prime number is a natural number greater than 1 that is divisible only by 1 and itself.
"""

import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_largest_prime(numbers):
    largest_prime = -1
    for num in numbers:
        if is_prime(num) and num > largest_prime:
            largest_prime = num
    return largest_prime