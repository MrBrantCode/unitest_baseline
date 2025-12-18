"""
QUESTION:
Create a function `prime_numbers(x, y)` that takes two parameters, x and y, and returns a list of all prime numbers between x and y (inclusive). The function should be efficient and handle large ranges of x and y.
"""

import math

def prime_numbers(x, y):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    return [num for num in range(x, y+1) if is_prime(num)]