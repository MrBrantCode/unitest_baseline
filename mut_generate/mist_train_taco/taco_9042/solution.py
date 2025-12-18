"""
QUESTION:
You are given 3 points - middles of the sides of some triangle. Find coordinates of the triangle vertices.

Input
Input  has 3 lines with 2 space-separated reals each - coordinates of the middles of the sides.

Output
Output 3 lines with 2 space-separated reals - coordinates of the triangle vertices. Each number should have exactly 4 digits after dot.  Vertices should be sorted in first coordinate ascending order. If two points have the same first coordinate than they should have second coordinate ascending order.

Constraints
0 ≤ xi, yi ≤ 1000

SAMPLE INPUT
5.00 3.00
4.0 4.0
5.0 5.000

SAMPLE OUTPUT
4.0000 2.0000
4.0000 6.0000
6.0000 4.0000
"""

def find_triangle_vertices(mid1, mid2, mid3):
    # Unpack the midpoint coordinates
    x1, y1 = mid1
    x2, y2 = mid2
    x3, y3 = mid3
    
    # Calculate the vertices
    a1 = x1 - x2 + x3
    a2 = 2 * x1 - a1
    a3 = 2 * x2 - a2
    
    b1 = y1 - y2 + y3
    b2 = 2 * y1 - b1
    b3 = 2 * y2 - b2
    
    # Create a list of vertices
    vertices = [(a1, b1), (a2, b2), (a3, b3)]
    
    # Sort the vertices
    vertices.sort()
    
    # Return the sorted vertices
    return vertices