"""
QUESTION:
Create a function `prime_product_trio(a)` that determines if a given number `a` (less than 1000) is the product of 3 distinct prime numbers. If it is, return a tuple containing the three prime factors; otherwise, return 'Not a product of 3 distinct prime numbers.' The function should handle cases where `a` has more than three prime factors, and it should efficiently check for primality.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_product_trio(a):
    """
    Determine if a given number is the product of 3 distinct prime numbers.
    
    Args:
    a (int): The input number to check.
    
    Returns:
    tuple or str: A tuple of three prime factors if a is their product; otherwise, 'Not a product of 3 distinct prime numbers.'
    """
    factors = set()
    for n in range(2, a):
        if a % n == 0 and is_prime(n):
            factors.add(n)
            if len(factors) > 3:
                return 'Not a product of 3 distinct prime numbers.'
    if len(factors) == 3:
        return tuple(factors)
    else:
        return 'Not a product of 3 distinct prime numbers.'