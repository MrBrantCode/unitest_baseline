"""
QUESTION:
Create a function `volume_of_torus(r, R)` that calculates the volume of a torus given the radius of the tube `r` and the distance from the center of the tube to the center of the torus `R`. The function should return the volume of the torus using the formula `(pi * r^2) * (2 * pi * R)`. The function should handle edge cases where `r` or `R` is 0.
"""

import math

def volume_of_torus(r, R):
    V = (math.pi * r**2) * (2 * math.pi * R)
    return V