"""
QUESTION:
Create a function called `prime_factors(n)` that takes a positive integer `n` and returns a list of all its prime factors. The function should be efficient and able to handle large inputs. Note that the input `n` is guaranteed to be a positive integer.
"""

def prime_factors(n):
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
    return factors