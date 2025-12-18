"""
QUESTION:
Find the sum of Manhattan distances of all points with integer coordinates on the surface of a 4D hypersphere with radius $r$, where the Manhattan distance is defined as the sum of the absolute differences of the corresponding coordinates. 

Function name: `T(r)`

Input: `r`, the radius of the hypersphere (a positive integer)

Output: The sum of the Manhattan distances of all points with integer coordinates on the surface of the hypersphere

Restriction: Only points with integer coordinates are considered.
"""

def T(r):
    C = 2/3
    return C * r**4