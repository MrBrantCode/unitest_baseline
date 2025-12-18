"""
QUESTION:
Implement a function, `filter_prime_numbers`, that takes a range of integers and returns a list of prime numbers within that range, excluding a specified number. The function should have a time complexity of O(log n), where n is the size of the range.

The function should take three parameters: `lower_bound`, `upper_bound`, and `excluded_number`. It should return a list of prime numbers in the range `[lower_bound, upper_bound)` that are not equal to `excluded_number`.
"""

import math

def filter_prime_numbers(lower_bound, upper_bound, excluded_number):
    """
    This function filters prime numbers in a given range excluding a specified number.
    
    Parameters:
    lower_bound (int): The lower bound of the range (inclusive).
    upper_bound (int): The upper bound of the range (exclusive).
    excluded_number (int): The number to be excluded from the prime numbers.
    
    Returns:
    list: A list of prime numbers in the range [lower_bound, upper_bound) excluding excluded_number.
    """
    prime_numbers = []
    for num in range(lower_bound, upper_bound):
        if num == excluded_number:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers