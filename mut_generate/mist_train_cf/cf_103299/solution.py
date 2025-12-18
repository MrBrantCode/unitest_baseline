"""
QUESTION:
Write a function named `power` that calculates the value of `base` raised to the power of `exp` using only basic arithmetic operations (addition, subtraction, multiplication, and division) and without using any built-in exponentiation or logarithmic functions. The function should take two parameters: `base` and `exp`, and return the result. Assume that the inputs `base` and `exp` are valid numbers.
"""

def power(base, exp):
    result = 1

    # If the exponent is negative, convert it to a positive exponent and take the reciprocal of the base
    if exp < 0:
        base = 1 / base
        exp = -exp

    # Perform multiplication in a loop
    for _ in range(exp):
        result *= base

    return result