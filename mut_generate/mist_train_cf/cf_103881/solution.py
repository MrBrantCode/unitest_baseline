"""
QUESTION:
Create a class named Circle with an initializer that takes in the x and y coordinates of the circle's center and the radius. The class should include three methods: circumference, area, and is_point_inside. The circumference method should return the circle's circumference, the area method should return the circle's area, and the is_point_inside method should take in the x and y coordinates of a point and return True if the point is inside the circle and False otherwise.
"""

import math

def circle_parameters(center_x, center_y, radius):
    def circumference():
        return 2 * math.pi * radius
    
    def area():
        return math.pi * (radius ** 2)
    
    def is_point_inside(point_x, point_y):
        distance = math.sqrt((point_x - center_x)**2 + (point_y - center_y)**2)
        return distance <= radius

    return circumference, area, is_point_inside

# circumference, area, is_point_inside = circle_parameters(0, 0, 5)
# print(circumference())  
# print(area())  
# print(is_point_inside(3, 4))  
# print(is_point_inside(6, 7))  