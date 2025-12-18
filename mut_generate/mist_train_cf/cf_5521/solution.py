"""
QUESTION:
Implement a function named `power` that takes two parameters: `base` and `exponent`. The function should calculate the result of `base` raised to the power of `exponent` using a recursive approach and return the result as a decimal number with 10 decimal places of precision. The function should be able to handle large exponents (up to 10^9 or higher), negative exponents, and non-integer exponents. The time complexity of the function should be O(log n).
"""

def power(base, exponent):
    # Base case: any number raised to the power of 0 is 1
    if exponent == 0:
        return 1.0

    # Recursive case for positive exponents
    if exponent > 0:
        half_power = power(base, exponent // 2)
        
        # If the exponent is even, square the result of half_power
        if exponent % 2 == 0:
            return half_power * half_power
        
        # If the exponent is odd, multiply the result of half_power by the base
        else:
            return half_power * half_power * base

    # Recursive case for negative exponents
    else:
        # Negate the exponent and recursively calculate the positive power
        return 1.0 / power(base, -exponent)