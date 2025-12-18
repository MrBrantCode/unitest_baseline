"""
QUESTION:
Implement the `modular_exponentiation` function that calculates the modular exponentiation of a given base, exponent, and modulus. The function should take three integer inputs: `base`, `exponent`, and `modulus`, and return the result of `(base^exponent) % modulus`. The function should be able to handle large inputs efficiently.
"""

def modular_exponentiation(base: int, exponent: int, modulus: int) -> int:
    result = 1
    base = base % modulus  # Reduce base to a smaller value to optimize computation
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1  # Equivalent to exponent // 2
        base = (base * base) % modulus
    return result