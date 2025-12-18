"""
QUESTION:
Create a function named `binomial_coefficient` that calculates the binomial coefficient for two non-negative integers `n` and `r` where `r` is less than or equal to `n`. The function should return the result as an integer.
"""

def binomial_coefficient(n, r):
    fact = 1 
    if r > n - r:
        r = n - r 
    for i in range(r):
        fact *= (n) - i 
        fact /= (i+1) 
    return int(fact)