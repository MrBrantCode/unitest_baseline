"""
QUESTION:
Create a function called `find_prime_square` that takes a list of numbers as input and returns the index of the first occurrence of a prime number which is also a perfect square in the list, along with the sum of all numbers before this index. If no such number is found, the function should return None.
"""

import math

def find_prime_square(lst):
    """Returns the index of the first occurrence of a prime number which is also a perfect square in lst.
    Also returns the sum of all numbers before this index."""
    
    for i, num in enumerate(lst):
        if num >= 2 and all(num % j != 0 for j in range(2, int(math.sqrt(num)) + 1)) and math.isqrt(num)**2 == num:
            return i, sum(lst[:i])
    
    # If no prime square is found, return None
    return None