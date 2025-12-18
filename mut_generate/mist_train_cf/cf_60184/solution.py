"""
QUESTION:
Write a function `complex_modulus_diff(a1, b1, a2, b2)` that calculates the modulus of the difference between two complex numbers `a1 + b1i` and `a2 + b2i`, where `a1`, `b1`, `a2`, and `b2` are the real and imaginary parts of the two complex numbers. The function should return the modulus of the difference.
"""

import cmath

def complex_modulus_diff(a1, b1, a2, b2):
    complex_num1 = complex(a1, b1)
    complex_num2 = complex(a2, b2)

    diff = complex_num1 - complex_num2

    modulus = abs(diff)

    return modulus