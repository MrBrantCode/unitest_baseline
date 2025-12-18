"""
QUESTION:
Implement a function `round_complex_numbers(array)` that rounds off a collection of complex numbers (real and imaginary parts separately) to the nearest integer. The rounding function should round up if the decimal part is 0.5 or above, and round down otherwise. However, if the real part of a complex number is between -1 and 1 (exclusive), it should not be rounded, while the imaginary component should still be rounded.
"""

def round_complex_numbers(array):
    result = []
    for cn in array:
        real = cn.real
        imag = cn.imag
        if not -1 < real < 1:
            if real >= (int(real) + 0.5):
                real = round(real + 0.5)
            else:
                real = round(real - 0.5)
        if imag >= (int(imag) + 0.5):
            imag = round(imag + 0.5)
        else:
            imag = round(imag - 0.5)
        result.append(complex(real, imag))
    return result