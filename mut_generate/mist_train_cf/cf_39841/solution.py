"""
QUESTION:
Implement a function `lattice_const_to_lammps_box` that takes as input the lengths and angles of the lattice constants in a crystal lattice, and returns the bounds, tilts, and rotation matrix for the LAMMPS box representation. 

The function should take a tuple of three float values for the lengths of the lattice vectors and a tuple of three float values for the angles between the lattice vectors in radians. It should return a tuple of three tuples for the lower and upper bounds for the x, y, and z dimensions of the LAMMPS box, a tuple of three float values for the tilt factors for the xy, xz, and yz dimensions of the LAMMPS box, and a 3x3 numpy array for the rotation matrix for the LAMMPS box.
"""

import numpy as np
from math import sin, cos, sqrt

def lattice_const_to_lammps_box(lengths, angles):
    a, b, c = lengths
    alpha, beta, gamma = angles

    bounds = ((0, a), (0, b * sin(gamma)), (0, c))
    tilts = (b * cos(gamma), 0, 0)

    rotation_matrix = np.array([
        [a, b * cos(gamma), c * cos(beta)],
        [0, b * sin(gamma), c * (cos(alpha) - cos(beta) * cos(gamma)) / sin(gamma)],
        [0, 0, c * sqrt(1 - cos(beta)**2 - ((cos(alpha) - cos(beta) * cos(gamma)) / sin(gamma))**2)]
    ])

    return bounds, tilts, rotation_matrix