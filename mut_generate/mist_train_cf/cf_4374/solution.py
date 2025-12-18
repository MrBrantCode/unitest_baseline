"""
QUESTION:
Write a function `calculate_power` that takes two numbers, `base` and `exp`, and returns the result of `base` raised to the power of `exp` using basic arithmetic operations (addition, subtraction, multiplication, and division) without using built-in exponentiation or logarithmic functions. The function should handle negative exponents and fractional exponents and have a time complexity of O(log(exp)).
"""

def calculate_power(base, exp):
    # Handle the case when the exponent is 0
    if exp == 0:
        return 1

    # Handle the case when the base is 0
    if base == 0:
        return 0

    # Handle negative exponents
    if exp < 0:
        base = 1 / base
        exp = -exp

    result = 1

    # Exponentiation by squaring
    while exp > 0:
        # If exp is odd, multiply the result by base
        if exp % 2 == 1:
            result *= base

        # Divide the exponent by 2 and square the base
        exp //= 2
        base *= base

    return result