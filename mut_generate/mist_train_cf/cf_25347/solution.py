"""
QUESTION:
Design a ComplexNumber class with private fields for the real and imaginary parts. The class should have a public method to calculate the magnitude of the complex number and a public method to increment both the real and imaginary parts by 1.
"""

def complex_number(real, imag):
    class ComplexNumber:
        def __init__(self, real, imag):
            self.__real = real
            self.__imag = imag

        def get_magnitude(self):
            return (self.__real ** 2 + self.__imag ** 2) ** 0.5

        def increment(self):
            self.__real += 1
            self.__imag += 1

    return ComplexNumber(real, imag)