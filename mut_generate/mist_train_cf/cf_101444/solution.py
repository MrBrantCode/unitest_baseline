"""
QUESTION:
Create a function named `find_prime_square` that takes a list of numbers as input and returns the index of the first prime number which is also a perfect square, along with the sum of all numbers before this index. The function should be optimized for scalability to handle large input lists.
"""

import math

def is_prime(n):
    """Returns True if n is a prime number, False otherwise"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_square(n):
    """Returns True if n is a perfect square, False otherwise"""
    return math.isqrt(n)**2 == n

def find_prime_square(lst):
    """Returns the index of the first occurrence of a prime number which is also a perfect square in lst.
    Also returns the sum of all numbers before this index."""
    # Calculate the sum of all numbers in lst
    total_sum = sum(lst)
    
    # Check each number in lst for primality and perfect squareness
    for i, num in enumerate(lst):
        if is_prime(num) and is_perfect_square(num):
            return i, sum(lst[:i])
    
    # If no prime square is found, return None
    return None