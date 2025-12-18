"""
QUESTION:
Create a function named `prime_factors` that takes an integer `num` and returns a list of its prime factors. The function should be able to handle numbers up to 1,000,000. The returned list should include all prime factors, even if they appear more than once.
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