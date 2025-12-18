"""
QUESTION:
Write a function named `get_second_to_last_prime` that takes a list of integers as input, and returns the second-to-last prime number in the list without using any built-in list methods. The input list may contain up to 10^6 elements, and all elements are integers between 1 and 10^6 (inclusive).
"""

import math

def get_second_to_last_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    prime_count = 0
    second_to_last_prime = None
    
    for num in reversed(numbers):
        if is_prime(num):
            prime_count += 1
            if prime_count == 2:
                second_to_last_prime = num
                break
    
    return second_to_last_prime