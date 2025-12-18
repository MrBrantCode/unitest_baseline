"""
QUESTION:
Create a function called `prime_factors` that takes a positive integer `num` and returns a list of its prime factors in ascending order. The function should not return any repeated factors and should be able to handle inputs up to 1,000,000 within a reasonable time limit.
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