"""
QUESTION:
Create a function named `prime_factors(n)` that takes a positive integer `n` as input and returns a list of its prime factors. The function should have a time complexity of O(sqrt(n)) and space complexity of O(1), and it should not use any built-in prime factorization functions or libraries, or external resources.
"""

def prime_factors(n):
    factors = []
    
    # Check if 2 is a prime factor
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for prime factors starting from 3
    i = 3
    while i*i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors