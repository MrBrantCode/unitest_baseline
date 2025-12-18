"""
QUESTION:
Implement a class `Transformation2D` with methods for performing 2D transformations and a function `compose_transformations` to combine two transformations. The `Transformation2D` class should have methods `__init__(self, x, y, theta)`, `translate(self, dx, dy)`, `rotate(self, dtheta)`, and `get_pose(self)`. The `compose_transformations(trans1, trans2)` function should take two `Transformation2D` objects as input and return a new `Transformation2D` object representing the composition of the two transformations, where `trans2` is applied first and then `trans1`.
"""

import numpy as np

class Transformation2D:
    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self, dtheta):
        self.theta += dtheta

    def get_pose(self):
        return self.x, self.y, self.theta

def composeTransformations(trans1, trans2):
    x1, y1, theta1 = trans1.get_pose()
    x2, y2, theta2 = trans2.get_pose()

    # Compose translation components
    x_new = x1 + np.cos(theta1) * x2 - np.sin(theta1) * y2
    y_new = y1 + np.sin(theta1) * x2 + np.cos(theta1) * y2

    # Compose rotation components
    theta_new = theta1 + theta2

    return Transformation2D(x_new, y_new, theta_new)