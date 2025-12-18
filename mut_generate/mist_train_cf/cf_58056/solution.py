"""
QUESTION:
Given a quadratic equation in the form ax^2 + bx + c, write a function `find_y_coordinate_of_vertex` that takes the coefficients `a`, `b`, and `c` as input and returns the y-coordinate of the vertex (k) in its vertex form a(x - h)^2 + k. The function should only use the given coefficients and the formula for the x-coordinate of the vertex (h = -b / 2a) to calculate k.
"""

def find_y_coordinate_of_vertex(a, b, c):
    h = -b / (2 * a)
    k = a * h**2 + b * h + c
    return k