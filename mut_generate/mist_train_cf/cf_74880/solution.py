"""
QUESTION:
Create a function called `sum_factors` that calculates the sum of all factors (including the number itself and 1) of a given integer. The function should take one integer argument `num` and return the sum of its factors.
"""

def sum_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return sum(factors)