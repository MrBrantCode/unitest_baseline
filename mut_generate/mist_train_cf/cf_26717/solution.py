"""
QUESTION:
Implement a function `calculate_positions_and_momenta` that calculates the positions and momenta of particles in a physical system. The function should take two parameters: `time_like`, a numerical value representing a specific time, and `return_cartesian`, a boolean flag indicating whether to return positions in Cartesian coordinates or momenta in Spherical Polar coordinates.

The function should return a tuple of three float values representing either the Cartesian coordinates (x, y, z) if `return_cartesian` is True or the Spherical Polar coordinates (r, theta, phi) if `return_cartesian` is False.
"""

from typing import Union, Tuple
import math

def calculate_positions_and_momenta(time_like: float, return_cartesian: bool) -> Union[Tuple[float, float, float], Tuple[float, float, float]]:
    if return_cartesian:
        x = time_like * 2.0  
        y = time_like * 3.0  
        z = time_like * 4.0  
        return x, y, z
    else:
        r = time_like * 1.5  
        theta = math.radians(45)  
        phi = math.radians(60)  
        return r, theta, phi