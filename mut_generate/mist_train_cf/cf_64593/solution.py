"""
QUESTION:
Design a function `calculate_total_force` that calculates the total gravitational force acting upon all celestial bodies in a solar system given their masses and positions in 3D space. The function should take a list of celestial bodies, where each body is defined by its mass and position (x, y, z), and return the total gravitational force acting on all bodies due to their pairwise interactions. Use the gravitational constant G = 6.67430e-11 and assume that all bodies are static with no velocity or acceleration.
"""

import math

G = 6.67430e-11  # gravitational constant

class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def calculate_force(body1_mass, body1_position, body2_mass, body2_position):
    dist_x = body2_position.x - body1_position.x
    dist_y = body2_position.y - body1_position.y
    dist_z = body2_position.z - body1_position.z
    distance = math.sqrt(dist_x ** 2 + dist_y ** 2 + dist_z ** 2)
    force = G * body1_mass * body2_mass / (distance ** 2)
    return force

def calculate_total_force(bodies):
    total_force = 0
    for i in range(len(bodies)):
        for j in range(i + 1, len(bodies)):
            force = calculate_force(bodies[i][0], bodies[i][1], bodies[j][0], bodies[j][1])
            total_force += force
    return total_force