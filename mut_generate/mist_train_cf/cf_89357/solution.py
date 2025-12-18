"""
QUESTION:
Write a function `find_maximum` that takes four arguments and returns the maximum of the four numbers using only ternary operators. The function should handle cases where two or more numbers are equal and should not use any other conditional statements.
"""

def find_maximum(a, b, c, d):
    max1 = a if a >= b else b
    max2 = c if c >= d else d
    maximum = max1 if max1 >= max2 else max2
    return maximum