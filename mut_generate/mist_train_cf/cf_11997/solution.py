"""
QUESTION:
Write a function `calculate_triangle_area` that calculates the area of a triangle given its three vertices A(x1, y1), B(x2, y2), and C(x3, y3) using the coordinates. The function should take six parameters (x1, y1, x2, y2, x3, y3) and return the calculated area.
"""

def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    """
    Calculate the area of a triangle given its three vertices.

    Args:
        x1 (float): The x-coordinate of vertex A.
        y1 (float): The y-coordinate of vertex A.
        x2 (float): The x-coordinate of vertex B.
        y2 (float): The y-coordinate of vertex B.
        x3 (float): The x-coordinate of vertex C.
        y3 (float): The y-coordinate of vertex C.

    Returns:
        float: The calculated area of the triangle.
    """
    area = 0.5 * abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))
    return area