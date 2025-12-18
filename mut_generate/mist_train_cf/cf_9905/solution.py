"""
QUESTION:
Write a function named prime_factorization to find the prime factors of a given number. The function should return the prime factors in the form of their product. For example, prime_factorization(153) should return '3 * 3 * 17'.
"""

def prime_factorization(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(str(i))
    if n > 1:
        factors.append(str(n))
    return ' * '.join(factors)