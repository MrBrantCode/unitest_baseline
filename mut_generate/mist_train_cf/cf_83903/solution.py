"""
QUESTION:
Create a function named `cube_root` that takes an integer `n` as input and returns its cube root accurate up to 2 decimal places. The integer `n` will be within the range of 1 to 64.
"""

def cube_root(n):
    return round(n ** (1. / 3.), 2)