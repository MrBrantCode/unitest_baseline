"""
QUESTION:
Implement a function named 'power' that takes two parameters, 'base' and 'exp', and calculates the value of 'base' raised to the power of 'exp' using only basic arithmetic operations (addition, subtraction, multiplication, and division). The function should handle both negative and fractional exponents.
"""

def power(base, exp):
    # handle negative exponents
    if exp < 0:
        return 1 / power(base, -exp)
    # handle fractional exponents
    if exp != int(exp):
        return base**(exp % 1) * power(base, int(exp))
    # base case
    if exp == 0:
        return 1
    result = base
    # multiply base by itself exp times
    for _ in range(1, int(exp)):
        result *= base
    return result