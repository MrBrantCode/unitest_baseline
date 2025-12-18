"""
QUESTION:
Design a function named `prime_product_quad` that takes an integer `b` less than 2000 as input and returns a tuple of four distinct prime factors if `b` is the product of four different prime numbers. Otherwise, it should return the string 'Not a product of 4 distinct prime numbers.'
"""

def prime_product_quad(b):
    """Return a tuple of four distinct prime factors if the provided number is a product of 4 different prime numbers, and return 'Not a product of 4 distinct prime numbers.' otherwise."""
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = set()
    for i in range(2, b + 1):
        if b % i == 0 and is_prime(i):
            factors.add(i)
            b //= i
        if len(factors) == 4:
            break
    return tuple(factors) if len(factors) == 4 and b == 1 else "Not a product of 4 distinct prime numbers."