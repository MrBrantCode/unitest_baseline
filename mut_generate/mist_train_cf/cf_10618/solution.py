"""
QUESTION:
Write a function `prime_factors(num)` to find all prime factors of a given integer `num`. The function should return a list of prime factors. The input number is a positive integer.
"""

def prime_factors(num):
    factors = []
    i = 2
    while i <= num:
        if num % i == 0:
            factors.append(i)
            num = num / i
        else:
            i += 1
    return factors