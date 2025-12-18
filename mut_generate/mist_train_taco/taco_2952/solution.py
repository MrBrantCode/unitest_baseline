"""
QUESTION:
Program the function distance(p1, p2) which returns the distance between the points p1 and p2 in n-dimensional space. p1 and p2 will be given as arrays.

Your program should work for all lengths of arrays, and should return -1 if the arrays aren't of the same length or if both arrays are empty sets.

If you don't know how to measure the distance between two points, go here:
http://mathworld.wolfram.com/Distance.html
"""

def calculate_distance(p1, p2):
    if len(p1) != len(p2) or len(p1) == 0:
        return -1
    return sum(((a - b) ** 2 for (a, b) in zip(p1, p2))) ** 0.5