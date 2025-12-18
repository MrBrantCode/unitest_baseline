"""
QUESTION:
Write a function that finds the smallest two-digit prime number "a" such that the product of "a" and the sum of its digits "b" is a valid product. The function should start with the smallest two-digit number (10) and keep incrementing by 1 until it finds a prime number. The function should return the prime number "a" and the resulting value of "b". 

The function should use helper functions to check if a number is prime and to calculate the sum of the digits of a number. The function should not take any parameters.
"""

import math

def digit_sum(n):
    """Calculate the summation of digits of a number"""
    return sum(int(d) for d in str(n))

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def entrance():
    """Find the smallest two-digit prime number "a" such that the product of "a" and the sum of its digits "b" is a valid product"""
    a = 10
    while True:
        # Calculate b
        b = a * digit_sum(a)
        
        # Check if a is prime
        if is_prime(a):
            return a, b
        
        # Increment a by 1 and try again
        a += 1