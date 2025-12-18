"""
QUESTION:
Write a function named `prime_factors` that takes a positive integer `num` as input and returns a list of its distinct prime factors in ascending order. The function should be able to handle inputs up to 10^9 and return the result within a reasonable time limit.
"""

def prime_factors(num):
    factors = []
    i = 2  # smallest prime factor
    
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            if i not in factors:
                factors.append(i)
    
    if num > 1:
        if num not in factors:
            factors.append(num)
    
    return factors