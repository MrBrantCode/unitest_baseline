"""
QUESTION:
Create a function `is_prime(n)` that determines whether a given integer `n` is a prime number or a composite number. The function should handle positive and negative integers, and it should be efficient for large inputs. The output should be a boolean value indicating whether the number is prime or not.
"""

def is_prime(n):
    """Check if integer n is a prime"""
    # Make sure n is a positive integer
    n = abs(int(n))
    # Simple cases
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # All other even numbers are not primes
    if not n & 1: 
        return False
    # Range starts with 3 and only needs to go up the square root of n
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True