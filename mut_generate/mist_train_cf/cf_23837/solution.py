"""
QUESTION:
Write a function called `heron_area(a, b, c)` that calculates the area of an acute angled triangle using Heron's formula, where `a`, `b`, and `c` are the lengths of the triangle's sides. The function should return the calculated area.
"""

def heron_area(a, b, c): 
    # calculate the semi-perimeter 
    s = (a + b + c) / 2

    # calculate the area 
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area