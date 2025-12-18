"""
QUESTION:
Create a function `area(a, b, c)` that calculates the area of a triangle given its side lengths `a`, `b`, and `c`. The function should use Heron's formula to compute the area. The input side lengths `a`, `b`, and `c` are positive numbers, and the function should return the area as a floating-point number.
"""

def area(a, b, c):
    s = (a + b + c) / 2
    return (s*(s-a)*(s-b)*(s-c)) ** 0.5