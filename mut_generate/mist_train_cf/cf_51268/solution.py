"""
QUESTION:
Write a function `prime_factorization_exponents` that takes an integer `n` as input and returns its prime factorization using exponents. The function should return a dictionary where the keys are prime factors of `n` and the values are their corresponding exponents. The function should not use any external libraries.
"""

def prime_factorization_exponents(n):
    prime_factorization = {}
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factorization[i] = prime_factorization.get(i, 0) + 1
    if n > 1:
        prime_factorization[n] = prime_factorization.get(n, 0) + 1
    return prime_factorization