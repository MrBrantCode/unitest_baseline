"""
QUESTION:
Write a function `calculate_power(base, exponent)` that calculates the value of `base` raised to the power of `exponent` without using the exponentiation operator or any built-in power function. The function should return the calculated power. Implement a loop that prints the first 10 powers of a given number using this function.
"""

def calculate_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result