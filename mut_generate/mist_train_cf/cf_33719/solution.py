"""
QUESTION:
Implement a function `min_rectangle_area(coordinates)` that takes a list of tuples representing the (x, y) coordinates of points on a 2D plane. The function should return the minimum area of a rectangle that can be formed by selecting four distinct points from the given set of coordinates. The function must consider all possible rectangles and return the smallest area, not just the area of the bounding box.
"""

def min_rectangle_area(coordinates):
    minx = float('inf')
    maxx = float('-inf')
    miny = float('inf')
    maxy = float('-inf')

    for newpx, newpy in coordinates:
        minx = min(minx, newpx)
        maxx = max(maxx, newpx)
        miny = min(miny, newpy)
        maxy = max(maxy, newpy)

    return (maxx - minx) * (maxy - miny)