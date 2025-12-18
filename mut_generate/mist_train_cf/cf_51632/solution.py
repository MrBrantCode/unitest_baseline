"""
QUESTION:
Create a function called `prime_factors(n)` that takes an integer `n` as input and returns a dictionary containing its prime divisors as keys and their corresponding counts as values. The function should be able to handle large input numbers up to 10^12 efficiently.
"""

def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i] = factors.get(i, 0) + 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors