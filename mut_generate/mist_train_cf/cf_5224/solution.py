"""
QUESTION:
Write a function `get_second_to_last_prime(numbers)` that takes a list of integers as input and returns the second-to-last prime number in the list. The list may contain up to 10^6 elements and all elements will be integers between 1 and 10^6 (inclusive). The function should not use any built-in list methods.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_second_to_last_prime(numbers):
    prime_count = 0
    second_to_last_prime = None
    
    for num in reversed(numbers):
        if is_prime(num):
            prime_count += 1
            if prime_count == 2:
                second_to_last_prime = num
                break
    
    return second_to_last_prime