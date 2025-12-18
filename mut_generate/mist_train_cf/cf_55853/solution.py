"""
QUESTION:
Create a function named `prime_factor_product` that takes an integer `n` as input and returns `True` if `n` is the product of exactly four distinct prime numbers, and `False` otherwise. The function should be optimized to handle integers less than 10,000.
"""

import math

def prime_factor_product(n):
    """Return true if n is a product of exactly four distinct prime numbers, false otherwise."""
    def is_prime(number):
        """Check if number is a prime number"""
        if number <= 1: 
            return False
        elif number <= 3: 
            return True
        elif number % 2 == 0 or number % 3 == 0: 
            return False
        i = 5
        while(i * i <= number): 
            if (number % i == 0 or number % (i + 2) == 0): 
                return False
            i += 6
        return True

    factors = []
    for count in range(2, math.isqrt(n) + 1): 
        if n % count == 0: 
            if(is_prime(count)): 
                factors.append(count)
            if(is_prime(n // count)): 
                factors.append(n // count)
    factors = list(set(factors))
    
    return True if len(factors) == 4 else False