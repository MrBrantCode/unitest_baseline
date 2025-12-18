"""
QUESTION:
Create a function called `get_factors` that takes an integer `num` as input and returns a list of all the factors of `num`, excluding 1 and `num` itself. The function should only consider integer factors.
"""

def get_factors(num):
    factors = []
    for i in range(2, num):
        if num % i == 0:
            factors.append(i)
    return factors