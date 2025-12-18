"""
QUESTION:
Create a function called `prime_factors` that takes an integer `num` as input, where 1 ≤ num ≤ 1,000,000, and returns a list of all prime factors of `num`.
"""

def prime_factors(num):
    factors = []
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors