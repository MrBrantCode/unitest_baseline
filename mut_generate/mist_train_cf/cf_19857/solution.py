"""
QUESTION:
Create a function named `is_prime` that takes an integer as input and returns a boolean value indicating whether the number is prime or not. The function should consider 2 as the smallest prime number and use an optimized approach to check for primality. The function should be used to find the sum, average, and count of all prime numbers between a given range `a` and `b` (inclusive) that also fall within a sub-range `c` and `d` (inclusive). The function should handle division by zero when calculating the average. 

Restrictions: The input values `a`, `b`, `c`, and `d` are integers, and `a` is less than or equal to `b`. Similarly, `c` is less than or equal to `d`.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True