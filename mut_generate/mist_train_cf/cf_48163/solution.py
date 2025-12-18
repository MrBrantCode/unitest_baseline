"""
QUESTION:
Create a function `check_prime` that takes a single integer argument `x` and returns a string indicating whether `x` is a 'Prime' or 'Composite' number. The function should use a modulus mathematical expression to determine the result, and it should only work for numbers greater than 1.
"""

def check_prime(x):
    return 'Composite' if len([i for i in range(2, round(x**0.5) + 1) if x % i == 0]) else 'Prime'