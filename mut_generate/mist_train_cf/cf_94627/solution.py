"""
QUESTION:
Create a function called `prime_factors` that takes a positive integer `n` as input and returns a list of its prime factors without using any built-in prime factorization functions or libraries. The function should have a time complexity of O(sqrt(n)) and a space complexity of O(1), not using any additional data structures to store the prime factors.
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