"""
QUESTION:
Create a function `calculate_gravitational_pull(m, h)` that takes two parameters: `m` (the mass of the object in kg) and `h` (the height of the object above the Earth's surface in meters). The function should calculate and return the gravitational pull on the object, applying the inverse square law for objects beyond 100km (100,000m) above the Earth's surface.
"""

import math

def calculate_gravitational_pull(m, h):
    G = 6.674 * math.pow(10, -11) 
    EARTH_RADIUS = 6.371 * math.pow(10, 6)
    EARTH_MASS = 5.972 * math.pow(10, 24)

    if h <= 100000: 
        F = (G * m * EARTH_MASS) / math.pow(EARTH_RADIUS + h, 2)
    else: 
        F = (G * m * EARTH_MASS) / math.pow(h, 2)
    
    return F