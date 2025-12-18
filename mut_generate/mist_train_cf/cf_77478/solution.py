"""
QUESTION:
Create a function named `recursive_prime_filter` that takes a list of integers (which may be nested) as input, identifies the prime numbers within the list, and returns them in a new list sorted in ascending order. The function should be able to handle nested lists of arbitrary depth.
"""

import math

def recursive_prime_filter(data):
    prime_numbers = []
    for item in data:
        if type(item) == list:
            prime_numbers.extend(recursive_prime_filter(item))
        elif type(item) == int:  
            if item > 1:  
                for i in range(2, math.isqrt(item) + 1):
                    if (item % i) == 0:
                        break
                else:
                    prime_numbers.append(item)
    return sorted(prime_numbers)