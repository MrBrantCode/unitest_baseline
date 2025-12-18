"""
QUESTION:
Create a function `calculate_torus_volume(r, R)` to calculate the volume of a torus using the formula `(pi * r^2) * (2 * pi * R)`, where 'r' is the radius of the tube and 'R' is the distance from the center of the tube to the center of the torus. Ensure the function only accepts positive numeric inputs for 'r' and 'R' and returns an error message for invalid inputs.
"""

import math

def calculate_torus_volume(r, R):
    if isinstance(r, (int, float)) and isinstance(R, (int, float)) and r > 0 and R > 0:
        volume = (math.pi * r**2) * (2 * math.pi * R)
        return volume
    else:
        return "Inputs should be positive numbers"