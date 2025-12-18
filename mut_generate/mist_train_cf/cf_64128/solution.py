"""
QUESTION:
Create a function named `polar_to_rectangular` that takes two parameters: the magnitude `r` and the angle `theta` in radians. The function should return the corresponding rectangular coordinates `(x, y)` using the mathematical principles of trigonometry. The `math` library can be used for the `cos` and `sin` functions.
"""

import math

def polar_to_rectangular(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)