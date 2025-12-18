"""
QUESTION:
Create a function to describe a geometric shape, either a rectangle or a circle, that can calculate the area, perimeter, and check if a given point is inside the shape. The function should be implemented using classes in Python.
"""

import math

def geometric_shape(width=None, height=None, radius=None):
    class GeometricShape:
        def __init__(self):
            self.shape_type = ""

        def calculate_area(self):
            pass

        def calculate_perimeter(self):
            pass

        def is_point_inside(self, point):
            pass

    class Rectangle(GeometricShape):
        def __init__(self, width, height):
            super().__init__()
            self.shape_type = "rectangle"
            self.width = width
            self.height = height

        def calculate_area(self):
            return self.width * self.height

        def calculate_perimeter(self):
            return 2 * (self.width + self.height)

        def is_point_inside(self, point):
            x, y = point
            return 0 <= x <= self.width and 0 <= y <= self.height

    class Circle(GeometricShape):
        def __init__(self, radius):
            super().__init__()
            self.shape_type = "circle"
            self.radius = radius

        def calculate_area(self):
            return math.pi * self.radius**2

        def calculate_perimeter(self):
            return 2 * math.pi * self.radius

        def is_point_inside(self, point):
            x, y = point
            distance = math.sqrt((x**2) + (y**2))
            return distance <= self.radius

    if width is not None and height is not None:
        return Rectangle(width, height)
    elif radius is not None:
        return Circle(radius)
    else:
        return None