"""
QUESTION:
Implement a function named `calculate_power` that takes two parameters, `base` and `exponent`, and calculates the power of `base` raised to the `exponent` without using the exponentiation operator or any built-in function that calculates powers. The function should return the calculated power. 

The function will be used in a loop that prints the first 10 powers of a given number `x`.
"""

def calculate_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result