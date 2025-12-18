"""
QUESTION:
Create a function `factorial_of_primes` that takes a list of numbers as input and returns a new list containing the factorials of the prime numbers from the original list. The function should ignore non-integer values and handle them without raising an error.
"""

import math

def factorial_of_primes(nums):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    result = []
    for num in nums:
        if isinstance(num, int) and is_prime(num):
            result.append(math.factorial(num))

    return result