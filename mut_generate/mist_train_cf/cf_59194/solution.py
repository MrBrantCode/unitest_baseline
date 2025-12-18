"""
QUESTION:
Create a "Point" class with two instance variables x and y, an initializer method, and two additional methods: length() and distance_to(other_point). The length() method should return the length of the vector from origin (0,0) to the point (x,y). The distance_to(other_point) method should return the Euclidean distance between this point and another point given as argument. The initializer method should take two parameters x and y and correctly assign them to their respective instance variables. The class should also include error checking to ensure other_point in distance_to(other_point) is an instance of the Point class.
"""

import math

def Point(x, y):
    return (x, y, math.sqrt(x**2 + y**2), lambda other_point: math.sqrt((x - other_point[0])**2 + (y - other_point[1])**2) if isinstance(other_point, tuple) else "other_point should be a point")