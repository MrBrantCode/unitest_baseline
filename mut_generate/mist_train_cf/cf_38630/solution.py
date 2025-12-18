"""
QUESTION:
Implement a Python class `Cbot` that represents a circular robot in a 2D space. The class should have the following properties and methods: 
- An initializer (`__init__`) that takes the robot's initial x-coordinate, y-coordinate, and radius as parameters.
- A method `move_to(x, y)` that updates the robot's position to the specified coordinates (x, y).
- A method `is_in_collision(x, y, obstacle_x, obstacle_y, obstacle_radius)` that determines if the robot will collide with an obstacle after moving to the specified coordinates (x, y), given the coordinates and radius of the obstacle. The collision is determined by checking if the distance between the robot's center and the obstacle's center is less than or equal to the sum of their radii. 

Note: Geometric calculations can be performed using the math library.
"""

import math

def is_in_collision(x, y, obstacle_x, obstacle_y, self_radius, obstacle_radius):
    distance = math.sqrt((x - obstacle_x) ** 2 + (y - obstacle_y) ** 2)
    return distance <= self_radius + obstacle_radius