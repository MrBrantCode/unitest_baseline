"""
QUESTION:
Implement a function named `delete_primes` that takes a list of integers as input and returns the modified list with all prime numbers removed. The input list may contain duplicate elements, and the function should not use any built-in functions or methods that directly delete elements from a list. The time and space complexity of the solution should be as efficient as possible.
"""

import math

def delete_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in lst:
        if not is_prime(num):
            result.append(num)
    return result