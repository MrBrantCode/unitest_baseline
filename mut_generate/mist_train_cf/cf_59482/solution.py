"""
QUESTION:
Create a function called `factorize_string` that takes a string input representing a whole number. Convert the input string to an integer, factorize it into prime numbers, and return an array of prime factors in ascending order. The input string is guaranteed to represent a whole number.
"""

def factorize_string(s):
    n = int(s)
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
    return sorted(factors)