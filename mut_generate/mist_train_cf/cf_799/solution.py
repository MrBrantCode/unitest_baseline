"""
QUESTION:
Write a function called `calculate_gravitational_force` that computes the gravitational force between multiple mass distributions using the formula F = G * ((m1 * m2) / r^2), where G is the gravitational constant (6.67430 x 10^-11 N*m^2/kg^2), m1 and m2 are the masses in kilograms, and r is the distance between the points in meters. The function should take a list of MassDistribution objects as input, where each MassDistribution object has attributes for the mass and position of each point. The function should return the total gravitational force between all pairs of points in different mass distributions.

The MassDistribution class should have an initializer method that takes the mass and position of a point as input. The position should be a tuple of three floats representing the x, y, and z coordinates of the point.

The function should use a helper function called `calculate_distance` to compute the distance between two points in space. This function should take two MassDistribution objects as input and return the Euclidean distance between their positions.

The function should have a time complexity of O(n^2), where n is the total number of points in all mass distributions.
"""

import math

class MassDistribution:
    def __init__(self, mass, position):
        self.mass = mass
        self.position = position

def calculate_distance(point1, point2):
    x1, y1, z1 = point1.position
    x2, y2, z2 = point2.position
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance

def calculate_gravitational_force(point1, point2):
    G = 6.67430e-11
    m1 = point1.mass
    m2 = point2.mass
    r = calculate_distance(point1, point2)
    force = G * ((m1 * m2) / r**2)
    return force