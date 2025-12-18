"""
QUESTION:
Implement the function G(n) to calculate the sum of the inradii of triangles inscribed in all possible ellipses defined by the equation x^2/a^2 + y^2/b^2 = 1, where a is greater than 2b and b >= 1. The inradius r of such a triangle is given by the formula r(a,b) = a/2 - b. 

The function G(n) should sum over all a from 3 to n and for each a, sum over all b from 1 to floor((a-1)/2). The result should be returned in scientific notation, rounded to 10 significant digits.
"""

import numpy as np

def G(n):
    a_values = np.arange(3, n+1)
    b_counts = (a_values - 1) // 2
    b_sums = b_counts * (b_counts + 1) / 2
    r_sums = a_values * b_counts / 2 - b_sums
    return np.sum(r_sums)