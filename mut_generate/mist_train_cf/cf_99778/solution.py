"""
QUESTION:
Generate the first n terms of a quadratic pattern represented by the polynomial equation n^2 + n + 1, starting from n=0. The function should be named generate_quadratic_pattern and take one integer parameter n. The function should return a list of integers representing the first n terms of the quadratic pattern.
"""

def generate_quadratic_pattern(n):
    return [i**2 + i + 1 for i in range(n)]