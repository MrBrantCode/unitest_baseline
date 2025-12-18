"""
QUESTION:
Write a function named `prism_volume` that calculates the volume of a triangular prism with a precision of 2 decimal points given its three sides `a`, `b`, `c`, and height `h`. The function should return -1 if the sides and height do not form a valid triangular prism, where a valid triangular prism satisfies the conditions: the sum of any two sides is greater than the length of the third side, and the height is greater than 0.
"""

def prism_volume(a, b, c, h):
    # validate if sides and height form a valid prism
    if a + b <= c or b + c <= a or a + c <= b or h <= 0:
        return -1
    p = (a + b + c) / 2
    # use math.sqrt instead of ^0.5 to compute the square root
    base_area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
    volume = base_area * h
    return round(volume, 2)