"""
QUESTION:
Create a function called `prime_factorization` that takes an integer as input and returns a list of its prime factors without using any built-in prime factorization functions or libraries. The function should divide the input number into its prime factors and return them as a list.
"""

def prime_factors(n):
    factors = []
    divisor = 2
    
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1
    
    return factors