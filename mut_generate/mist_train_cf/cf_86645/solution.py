"""
QUESTION:
Create a function `find_hcf(a, b)` that calculates the highest common factor (HCF) of two integers `a` and `b` without using the modulus operator (`%`) or any built-in functions that directly calculate the HCF. The function should return the HCF of `a` and `b`.
"""

def find_hcf(a, b):
    while b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a