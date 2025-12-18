"""
QUESTION:
Develop a function called `perform_operation` that takes as input an operation (addition, subtraction, multiplication, or division) and two complex numbers `a` and `b`, each represented as a real part and an imaginary part. The function should perform the specified operation on `a` and `b`, handling the real and imaginary parts separately, and return the result as a complex number.
"""

class ComplexNumber:
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def add(self, no):
        real = self.real + no.real
        imag = self.imag + no.imag
        return ComplexNumber(real, imag)

    def subtract(self, no):
        real = self.real - no.real
        imag = self.imag - no.imag
        return ComplexNumber(real, imag)

    def multiply(self, no):
        real = self.real * no.real - self.imag * no.imag
        imag = self.real * no.imag + self.imag * no.real
        return ComplexNumber(real, imag)

    def divide(self, no):
        real = (self.real * no.real + self.imag * no.imag) / (no.real**2 + no.imag**2)
        imag = (self.imag * no.real - self.real * no.imag) / (no.real**2 + no.imag**2)
        return ComplexNumber(real, imag)

    def __repr__(self):
        return f"{self.real} + {self.imag}i"


def perform_operation(operation, a, b):
    operations = {
        'addition': a.add(b),
        'subtraction': a.subtract(b),
        'multiplication': a.multiply(b),
        'division': a.divide(b),
    }
    return operations[operation]