"""
QUESTION:
Implement a function `totalTriangleArea` that takes a list of tuples, where each tuple contains six numbers representing the x and y coordinates of the vertices of a triangle in the order (x1, y1, x2, y2, x3, y3). The function should return the total area of all triangles combined. Assume that the input coordinates are valid and form non-degenerate triangles.
"""

def totalTriangleArea(triangles):
    def calculateArea(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

    return sum(calculateArea(*triangle[:3], *triangle[3:]) for triangle in triangles)