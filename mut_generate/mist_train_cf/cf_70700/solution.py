"""
QUESTION:
Write a function `T(n)` that calculates the number of 60-degree triangles with integer sides where the radius of the inscribed circle is less than or equal to `n`. The function should return the count of such triangles. The input `n` is a positive integer.
"""

import math

def T(n):
    return math.floor(n / math.sqrt(3))