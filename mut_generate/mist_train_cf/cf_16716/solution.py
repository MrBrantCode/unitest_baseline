"""
QUESTION:
Write a function called `sum_prime_divisible_by_2_and_3` that takes an array of integers as input and returns the sum of elements that are divisible by both 2 and 3, and are prime numbers.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_prime_divisible_by_2_and_3(arr):
    sum_elements = 0
    for num in arr:
        if num % 2 == 0 and num % 3 == 0 and is_prime(num):
            sum_elements += num
    return sum_elements