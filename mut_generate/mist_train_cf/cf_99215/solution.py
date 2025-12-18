"""
QUESTION:
Write a function named `shoelace` and `perimeter` that calculates the area and perimeter of a polygonal shape given a set of points with distinct x-coordinates in the order they are connected. The function should assume the input points form a convex polygon and do not have any self-intersections. The function should return the calculated area and perimeter. The time complexity of the `shoelace` function should be O(n), where n is the number of points, and the time complexity of the `perimeter` function should be optimized to O(n) using dynamic programming if necessary.
"""

def shoelace(points):
    """
    Calculate the area of a polygon using the Shoelace formula.

    Args:
        points (list): A list of tuples representing the points of the polygon.

    Returns:
        float: The area of the polygon.
    """
    n = len(points)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1] - points[j][0] * points[i][1]
    return abs(area) / 2

def perimeter(points):
    """
    Calculate the perimeter of a polygon using the distance formula.

    Args:
        points (list): A list of tuples representing the points of the polygon.

    Returns:
        float: The perimeter of the polygon.
    """
    def distance(p1, p2):
        return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

    n = len(points)
    p = 0
    for i in range(n):
        j = (i + 1) % n
        p += distance(points[i], points[j])
    return p