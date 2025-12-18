"""
QUESTION:
Write a function `find_second_largest_prime` that takes an array of integers as input and returns the second largest unique prime number in the array. The array may contain duplicates. The function should return the minimum possible integer value if there are less than two unique prime numbers in the array.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_second_largest_prime(numbers):
    max_prime = float('-inf')
    second_max_prime = float('-inf')

    for num in numbers:
        if num > max_prime and is_prime(num):
            second_max_prime = max_prime
            max_prime = num
        elif num > second_max_prime and num != max_prime and is_prime(num):
            second_max_prime = num

    return second_max_prime