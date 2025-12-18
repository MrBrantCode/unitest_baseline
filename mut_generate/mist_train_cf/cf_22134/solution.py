"""
QUESTION:
Create a function `get_prime_numbers` that takes an array 'a' as input, containing at least 100 elements. The function should return a new array 'b' containing only the prime numbers from 'a', sorted in descending order.
"""

import math

def get_prime_numbers(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    return sorted([num for num in a if is_prime(num)], reverse=True)