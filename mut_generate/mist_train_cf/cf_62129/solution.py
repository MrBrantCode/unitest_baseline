"""
QUESTION:
Implement the `is_prime(n)` function to determine whether an integer `n` is prime or not, returning `True` for prime numbers and `False` for non-prime numbers. The function should be efficient and only check divisibility up to the square root of `n`. It should handle numbers less than 2 as non-prime.
"""

def is_prime(n):
    """Returns true for prime integers, false for non-prime integers."""

    # Case for numbers less than 2 (0, 1, and negatives), which are not prime
    if n < 2: 
        return False
  
    # Check divisibility up to the square root of n, any factor larger than the square root would need to be paired 
    # with a factor smaller than the square root.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True