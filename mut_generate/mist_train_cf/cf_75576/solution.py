"""
QUESTION:
Create a function named `complex_mult` that takes two complex numbers as input in the form of tuples, where each tuple contains the real part and the imaginary part of a complex number. The function should return a tuple representing the product of the two input complex numbers, calculated manually using the algebraic formula for complex number multiplication: `(ac-bd) + (bc+ad)i`, where `a`, `b`, `c`, and `d` are the real and imaginary parts of the two input complex numbers.
"""

def complex_mult(c1, c2):
    a = c1[0]
    b = c1[1]
    c = c2[0]
    d = c2[1]

    real = a*c - b*d
    imag = b*c + a*d

    return (real, imag)