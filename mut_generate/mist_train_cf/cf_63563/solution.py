"""
QUESTION:
Write a function called `cumulative_factorial_sum` that computes the cumulative total of the factorial values of all prime numbers within the range of 1 through to and including n. The function should take an integer n as input and return the cumulative total.
"""

from math import factorial

def cumulative_factorial_sum(n):
    """Compute the cumulative total of the factorial values of all prime numbers in the range 1 to n inclusively"""
    
    def is_prime(num):
        """Check if num is a prime number"""
        
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    total = 0
    for i in range(1, n + 1):
        if is_prime(i):
            total += factorial(i)
    return total