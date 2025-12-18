"""
QUESTION:
Define a function H(n) that calculates the number of points not directly visible from the center in a hexagonal orchard of order n. The function should take an integer n as input and return the number of obscured points. The function should handle the base cases where n is 1 or 2, and for larger n, it should use the formula 3*(n-2)^2 - 3*(n-2) + 6*(n-2)*(n-4) to calculate the number of obscured points. The function should be able to compute H(100000000).
"""

def H(n):
    if n <= 2:
        return 0
    else:
        return 3*(n-2)**2 - 3*(n-2) + 6*(n-2)*(n-4)