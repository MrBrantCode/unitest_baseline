"""
QUESTION:
Create a function named `prime_factor_count` that calculates the count of prime factors of a given number. Then, use this function to create a dictionary with elements from a tuple as keys and their corresponding prime factor counts as values. The function should not use any library functions for prime factorization.
"""

def prime_factor_count(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return len(factors)