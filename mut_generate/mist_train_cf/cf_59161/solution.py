"""
QUESTION:
Create a function called `solve_complex_eq` that takes three complex numbers `x`, `y`, and `z` as input, and returns a boolean indicating whether the equation `(2 + 3i)x + (1 - 4i)y - (5 + 2i)z` equals `7 - 9i`.
"""

def solve_complex_eq(x, y, z):
    return ((2 + 3j)*x + (1 - 4j)*y - (5 + 2j)*z) == (7 - 9j)