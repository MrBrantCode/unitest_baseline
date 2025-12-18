"""
QUESTION:
Implement a function named `diff_complex_nums` that takes two complex numbers as input and returns the absolute difference between them, defined as `abs(a-b)`. This function should utilize a corrected version of the provided `ComplexNumber` class.
"""

class ComplexNumber:
    def __init__(self, realpart=0, imagpart=0):
        self.real = realpart
        self.imag = imagpart

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)

    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5

def diff_complex_nums(a, b):
    return abs(a - b)