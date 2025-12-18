"""
QUESTION:
Write a function called `calculate_triangle_area(vertices)` that takes a list of three tuples representing the (x, y) coordinates of a triangle's vertices and returns the area of the triangle. The formula to calculate the area is: 0.5 * |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|. The function should return the absolute area, regardless of the order of the input vertices. The input is a list of three tuples, each containing two numbers representing the x and y coordinates of a vertex.
"""

def calculate_triangle_area(vertices):
    x1, y1 = vertices[0]
    x2, y2 = vertices[1]
    x3, y3 = vertices[2]
    
    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return area