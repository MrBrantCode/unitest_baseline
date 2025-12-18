"""
QUESTION:
Write a recursive function named `power(base, exp)` to calculate the power of two numbers (base^exp) without using any predefined power function. The function should handle invalid inputs and exceptions, such as negative exponents or a zero base with a non-zero exponent, and return an error message for these cases. Both the base and exponent must be numbers (int or float).
"""

def entance(base, exp):
    if not (isinstance(base, (int, float)) and isinstance(exp, (int, float))):
        return "Error: both base and exponent must be numbers"
    if base == 0 and exp <= 0:
        return "Error: 0 raised to a non positive number is undefined"
    if exp < 0:
        return "Error: the function does not support negative exponents"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp % 2 == 0:
        return entance(base * base, exp // 2)
    else:
        return base * entance(base * base, (exp - 1) // 2)