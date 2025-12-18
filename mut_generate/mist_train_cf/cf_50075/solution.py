"""
QUESTION:
Create a function `sum_of_primes(start, end)` to calculate the sum of all prime numbers in the range of consecutive integers from `start` to `end` (inclusive), where `start` and `end` are positive integers. The function should return the total sum of prime numbers in the given range.
"""

def is_prime(n):
    """Check if number is a prime number."""
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, int(n**0.5) + 1):
            if n % x == 0:
                return False
        return True            

def sum_of_primes(start, end):
    """Calculate sum of prime numbers between start and end"""
    total = 0
    for x in range(start, end+1):
        if is_prime(x):
            total += x
            
    return total