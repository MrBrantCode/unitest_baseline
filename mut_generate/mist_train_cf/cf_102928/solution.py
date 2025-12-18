"""
QUESTION:
Write a function named "calculate_area" that takes in six parameters: x1, y1, x2, y2, x3, y3 representing the coordinates of the three vertices of a triangle. The function should return the area of the triangle, assuming the given coordinates will always form a valid triangle.
"""

def calculate_area(x1, y1, x2, y2, x3, y3):
    # Calculate the area using the formula: 1/2 * |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)