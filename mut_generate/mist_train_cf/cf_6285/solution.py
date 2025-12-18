"""
QUESTION:
Write a function `find_maximum(a, b, c, d)` that finds the maximum of four numbers using only ternary operators. The function should take four integer arguments and return the maximum value among them. Ensure that the function correctly handles cases where two or more numbers are equal.
"""

def find_maximum(a, b, c, d):
    max1 = a if a >= b else b
    max2 = c if c >= d else d
    maximum = max1 if max1 >= max2 else max2
    return maximum