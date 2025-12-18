"""
QUESTION:
Create a function `max_triangle_area` that takes a list of 2D coordinates as input and returns the three points that form the triangle with the maximum area. The area of a triangle with vertices at (x1, y1), (x2, y2), and (x3, y3) is computed as 1/2 * |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)|. The function should consider all combinations of three points from the input list.
"""

def max_triangle_area(points):
    """
    This function calculates the three points that form the triangle with the maximum area.

    Parameters:
    points (list): A list of 2D coordinates.

    Returns:
    tuple: A tuple of three points forming a triangle with maximum area.
    """

    def calculate_area(point1, point2, point3):
        """
        This function calculates the area of a triangle given three points.

        Parameters:
        point1 (tuple): The first point.
        point2 (tuple): The second point.
        point3 (tuple): The third point.

        Returns:
        float: The area of the triangle.
        """
        x1, y1 = point1
        x2, y2 = point2
        x3, y3 = point3
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

    max_area = 0
    max_triangle = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                area = calculate_area(points[i], points[j], points[k])
                if area > max_area:
                    max_area = area
                    max_triangle = (points[i], points[j], points[k])

    return max_triangle