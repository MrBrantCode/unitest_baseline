"""
QUESTION:
Write a function `product_of_complex` that takes an array of complex numbers as input and returns their product. The input array is a list of complex numbers, where each complex number is represented by its real and imaginary parts.
"""

def product_of_complex(arr):
    result = complex(1, 0)
    for c in arr:
        result *= c
    return result