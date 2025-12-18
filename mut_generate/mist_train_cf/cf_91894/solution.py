"""
QUESTION:
Create a `Circle` class with a constructor that takes in the radius, color, and center coordinates (x, y) as parameters. The class should have methods to calculate the area, circumference, check if a point is inside the circle, and translate the circle by a given distance. The circle is considered filled, meaning any point on or inside the circumference is considered inside.
"""

import math

def entrance(radius, color, x, y):
    class Circle:
        def __init__(self, radius, color, center):
            self.radius = radius
            self.color = color
            self.center = center
        
        def get_area(self):
            return math.pi * self.radius**2
        
        def get_circumference(self):
            return 2 * math.pi * self.radius
        
        def is_point_inside(self, x, y):
            distance = math.sqrt((x - self.center[0])**2 + (y - self.center[1])**2)
            return distance <= self.radius
        
        def translate(self, dx, dy):
            self.center = (self.center[0] + dx, self.center[1] + dy)
    return Circle(radius, color, (x, y))