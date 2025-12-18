"""
QUESTION:
Write a function `find_second_largest_prime` that takes a list of integers as input and returns the second largest unique prime number in the list. The function should ignore duplicates and return the second largest prime number if it exists, otherwise return the result based on the implemented logic.
"""

import math

def find_second_largest_prime(numbers):
    max_prime = float('-inf')
    second_max_prime = float('-inf')
    unique_nums = set(numbers)  

    for num in unique_nums:
        if num > max_prime and is_prime(num):
            second_max_prime = max_prime
            max_prime = num
        elif num > second_max_prime and is_prime(num) and num != max_prime:
            second_max_prime = num

    return second_max_prime


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True