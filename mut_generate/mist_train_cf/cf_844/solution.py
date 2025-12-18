"""
QUESTION:
Create a function `find_hcf(a, b)` that takes two integers `a` and `b` as input and returns their highest common factor (HCF) without using the modulus operator or any built-in functions that directly calculate the HCF.
"""

def find_hcf(a, b):
    while b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a