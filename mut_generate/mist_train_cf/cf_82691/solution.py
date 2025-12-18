"""
QUESTION:
Find T(n) as the sum of the areas of all triangles with sides √(1+d^2), √(1+e^2), and √(d^2+e^2) (for positive integers d and e) that have an integral area not exceeding n. 

Implement a function T(n) that takes an integer n as input and returns the sum of the areas of all such triangles.
"""

from math import sqrt

def T(n):
    total = 0
    limit = int(sqrt(n//2)) + 1
    for m in range(2, limit, 2):
        for k in range(1, m, 2):
            a = m*m - k*k
            b = 2*m*k
            primitive_area = a*b//2
            if primitive_area > n:
                break
            total += (n // primitive_area) * primitive_area
    return total