"""
QUESTION:
Create a function named `complex_shape_area` that calculates the area of a complex pentagon or hexagon given its vertices' coordinates. The coordinates can be in counter-clockwise or clockwise order. The function should be able to handle any convex, non-intersecting polygon. Develop the function by dividing the polygon into triangles and summing their areas.
"""

def complex_shape_area(coordinates):
    """Using input values representing the coordinates of the vertices of the shape, accurately calculate the shape's area.
    """

    def triangle_area(x1, y1, x2, y2, x3, y3):
        """Helper function to calculate an area of a triangle."""
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))) / 2.0

    area = 0.0
    n = len(coordinates)  # number of vertices
    for i in range(n-2):  # Corrected the loop to only create triangles with the first point as a common vertex
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[i+1]  
        x3, y3 = coordinates[i+2]
        area += triangle_area(x1, y1, x2, y2, x3, y3)
    return area