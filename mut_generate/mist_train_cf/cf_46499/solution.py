"""
QUESTION:
Calculate the aggregate exterior space encompassing multiple spherical objects in a 3-dimensional space. The function should take as input a list of sphere coordinates and their corresponding radii, and return the total exterior space. The function should also account for intersections between spheres. 

Note: The function should assume that the input spheres have radii between 1 to 6 meters. 

Function name: `calculate_total_exterior_space`
"""

import math
from itertools import combinations

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def intersects(self, other):
        distance_centers = math.sqrt((self.center[0] - other.center[0]) ** 2 + (self.center[1] - other.center[1]) ** 2 + (self.center[2] - other.center[2]) ** 2)
        return distance_centers < (self.radius + other.radius)

def calculate_total_exterior_space(spheres):
    spheres_obj = [Sphere((sphere[0], sphere[1], sphere[2]), sphere[3]) for sphere in spheres]
    total_volume = sum([sphere_volume(sphere.radius) for sphere in spheres_obj])
    intersections = sum([s1.intersects(s2) for s1, s2 in combinations(spheres_obj, 2)])
    return total_volume - intersections