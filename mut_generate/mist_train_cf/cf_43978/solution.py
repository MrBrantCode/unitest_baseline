"""
QUESTION:
Write a function `prime_product(a)` that takes an integer `a` as input and returns a tuple of two or three distinct prime factors or the same prime number twice if `a` can be expressed as the product of 2 or 3 unique prime numbers or as the square of a prime number. If `a` cannot be expressed in this form, return 'Not a product of unique prime numbers.' The function should have a complexity of O(sqrt(a)). The value of `a` can be as high as 50,000.
"""

def prime_product(a):
    """
    Returns a tuple of two or three distinct prime factors or the same prime number twice 
    if 'a' can be expressed as the product of 2 or 3 unique prime numbers or as the square of a prime number.
    
    If 'a' cannot be expressed in this form, returns 'Not a product of unique prime numbers.'

    Parameters:
    a (int): The input number to find prime factors for.

    Returns:
    tuple: A tuple of prime factors or a message if 'a' cannot be expressed as the product of unique prime numbers.
    """
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = []
    if is_prime(a):
        return (a,)  # Return a tuple containing the prime number
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0 and is_prime(i):
            factors.append(i)
            if is_prime(a // i):
                factors.append(a // i)
    factors = sorted(list(set(factors)))
    if len(factors) > 3:
        return 'Not a product of unique prime numbers.'
    return tuple(factors)