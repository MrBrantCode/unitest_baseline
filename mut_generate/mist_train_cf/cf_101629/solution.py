"""
QUESTION:
Write a function `area_of_trapezoid(a, b, c, d)` that calculates the area of a trapezoid with parallel sides of length `a` and `b`, and non-parallel sides of length `c` and `d`, given that `a + b + c + d = 20` and `c > d`. The function should take into account that the trapezoid is not a square, has at least one pair of parallel sides, and has rotational symmetry of order 4. The area should be calculated using the formula `A = (h/2)(a+b)`, where `h` is the height of the trapezoid.
"""

def area_of_trapezoid(a, b, c, d):
    h = abs(c - d) / 2
    return (h * (a + b)) / 2