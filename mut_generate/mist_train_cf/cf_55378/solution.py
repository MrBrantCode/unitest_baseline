"""
QUESTION:
Write a function `cartesian_to_spherical` that takes a list of 3D Cartesian coordinates as input, where each point is represented by a tuple (x, y, z), and returns the corresponding spherical coordinates as a list of tuples (r, theta, phi). The radial distance r, polar angle theta, and azimuthal angle phi should be calculated using the formulas r = sqrt(x² + y² + z²), theta = arctan2(sqrt(x²+y²), z), and phi = arctan2(y, x), respectively. The angles theta and phi should be returned in radians, with theta in the interval [0, π] and phi in the interval [-π, π].
"""

import numpy as np

def cartesian_to_spherical(coords):
    spherical_coords = []
    for x,y,z in coords:
        r = np.sqrt(x**2 + y**2 + z**2)
        theta = np.arctan2(np.sqrt(x**2+y**2), z)
        phi = np.arctan2(y, x)
        spherical_coords.append((r, theta, phi))
    return spherical_coords