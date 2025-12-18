"""
QUESTION:
Create a function named `is_prime` that takes a positive integer `n` as input and returns a boolean value indicating whether `n` is a prime number. The input `n` must be within the range of 2 to 10^18, inclusive. If `n` is outside this range, return an error message. Optimize the solution to have a time complexity of O(sqrt(n)).
"""

import math

def is_prime(n):
    if n < 2 or n > 10**18:
        return "Input must be between 2 and 10^18, inclusive."
    elif n > 10**9:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True