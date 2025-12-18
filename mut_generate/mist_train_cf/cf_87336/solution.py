"""
QUESTION:
Write a function called `calculate_power` that takes two parameters: `base` and `exponent`. This function should return the result of `base` raised to the power of `exponent` without using any mathematical operators or built-in functions for exponentiation. The function should have a time complexity of O(log n) or better.
"""

def calculate_power(base, exponent):
    # Base case
    if exponent == 0:
        return 1
    
    # Split the exponent in half
    exp_half = exponent // 2
    
    # Recursively calculate the value of base to the power of exp_half
    value_half = calculate_power(base, exp_half)
    
    # Multiply the result by itself
    result = value_half * value_half
    
    # Multiply by the base if the exponent is odd
    if exponent % 2 == 1:
        result *= base
    
    return result